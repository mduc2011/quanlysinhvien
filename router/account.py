from fastapi import APIRouter,Header
from database import SessionLocal
from pydantic import BaseModel
from model import account as Account,RefreshToken
from auth import hash_password, verify_password,create_access_token,create_refresh_token\
    ,create_refresh_token\
    ,verify_token
from datetime import datetime, timedelta

class AccountSchema(BaseModel):
    email: str
    password: str

class RefreshShema(BaseModel):
    refresh_token: str

router=APIRouter()
@router.post("/account/register")
def register_account(account: AccountSchema):
    db=SessionLocal()
    if db.query(Account).filter(Account.username==account.email).first():
        return {"message":"Email đã tồn tại"}
    account.password=hash_password(account.password)
    db.add(Account(username=account.email,password=account.password))
    db.commit()
    db.close()
    return {"message":"Đăng ký thành công"}

@router.post("/account/login")
def login_account(account: AccountSchema):
    db=SessionLocal()
    acc=db.query(Account).filter(Account.username==account.email).first()
    if not acc:
        return {"message":"Email không tồn tại"}
    if not verify_password(account.password,acc.password):
        return {"message":"Mật khẩu không đúng"}
    access_token=create_access_token({"sub":acc.username})                #cấp token 
    refresh_token=create_refresh_token({"sub":acc.username})
    expired = (datetime.utcnow() + timedelta(days=7)).isoformat()
    rt = RefreshToken(
        token      = refresh_token,
        account_id = acc.id,
        expired_at = expired
    )
    db.add(rt)
    db.commit()
    db.close()
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
        }

@router.post("/account/refresh")
def refresh_access(data:RefreshShema):
    db=SessionLocal()
    rt=db.query(RefreshToken).filter(RefreshToken.token==data.refresh_token).first()

    if not rt:
        db.close()
        return {"message": "Refresh token không hợp lệ"}

    # Kiểm tra hết hạn
    if datetime.utcnow() > datetime.fromisoformat(rt.expired_at):
        db.close()
        return {"message": "Refresh token đã hết hạn"}
    payload = verify_token(data.refresh_token)
    new_access_token = create_access_token({"sub": payload["sub"]})

    db.close()
    return {"access_token": new_access_token}

@router.post("/account/logout")
def logout_account(data: RefreshShema):
    db=SessionLocal()

    rt=db.query(RefreshToken).filter(RefreshToken.token==data.refresh_token).first()

    if not rt :
        return {"messeger": "sai token"}
    db.delete(rt)
    db.commit 
    db.close
    return {"messeger": "da dang xuat"}



