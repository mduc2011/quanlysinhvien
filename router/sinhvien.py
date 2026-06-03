from model import sinhvien as SinhVien
from fastapi import APIRouter, Header
from database import SessionLocal
from pydantic import BaseModel
from auth import verify_token

router=APIRouter()

class SinhVienSchema(BaseModel):
    name: str
    age: int
    email: str
    lop: str

@router.post("/sinhvien")
def create_sinhvien(sinhvien: SinhVienSchema,token: str=Header(None)):
    if not token:
     return {"message": "Token không hợp lệ"}
    token= token.replace("Bearer ","")
    if not verify_token(token):
        return {"message":"Token không hợp lệ"}
    db=SessionLocal()
    new_sinhvien=SinhVien(name=sinhvien.name,age=sinhvien.age,email=sinhvien.email,lop=sinhvien.lop)
    db.add(new_sinhvien)
    db.commit()
    db.close()
    return {"message":"Sinh viên đã được tạo"}

@router.get("/sinhvien/{id}")
def get_sinhvien(id: int ,token: str=Header(None)):
    if not token:
     return {"message": "Token không hợp lệ"}
    token= token.replace("Bearer ","")
    if not verify_token(token):
        return {"message":"Token không hợp lệ"}
    db=SessionLocal()
    sinhvien=db.query(SinhVien).filter(SinhVien.id==id).first()
    db.close()
    return sinhvien

@router.get("/sinhvien")
def get_allsinhvien(token: str=Header(None)):
    if not token:
     return {"message": "Token không hợp lệ"}
    token= token.replace("Bearer ","")
    if not verify_token(token):
        return {"message":"Token không hợp lệ"}
    db=SessionLocal()
    sinhviens=db.query(SinhVien).all()
    db.close()
    return {"sinhviens":sinhviens}
@router.put("/sinhvien/update/{id}")
def update_sinhvien(id: int, sinhvien: SinhVienSchema, token: str=Header(None)):
    if not token:
        return {"message": "Token không hợp lệ"}
    token = token.replace("Bearer ", "")
    if not verify_token(token):
        return {"message": "Token không hợp lệ"}
    db = SessionLocal()
    db_sinhvien = db.query(SinhVien).filter(SinhVien.id == id).first()
    if not db_sinhvien:
        return {"message": "Sinh viên không tồn tại"}
    for key, value in sinhvien.dict().items():
        setattr(db_sinhvien, key, value)
    db.commit()
    db.close()
    return {"message": "Sinh viên đã được cập nhật"}

@router.delete("/sinhvien/delete/{id}")
def delete_sinhvien(id: int, token: str=Header(None)):
    if not token:
        return {"message": "Token không hợp lệ"}
    token = token.replace("Bearer ", "")
    if not verify_token(token):
        return {"message": "Token không hợp lệ"}
    db = SessionLocal()
    db_sinhvien = db.query(SinhVien).filter(SinhVien.id == id).first()
    if not db_sinhvien:
        return {"message": "Sinh viên không tồn tại"}
    db.delete(db_sinhvien)
    db.commit()
    db.close()
    return {"message": "Sinh viên đã được xóa"}