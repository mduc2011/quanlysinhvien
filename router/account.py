from fastapi import APIRouter
from database import SessionLocal
from pydantic import BaseModel
from model import account as Account
from auth import hash_password, verify_password, create_token, verify_token

class AccountSchema(BaseModel):
    email: str
    password: str

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
    token=create_token({"sub":acc.username})
    db.close()
    return {"token": token}
