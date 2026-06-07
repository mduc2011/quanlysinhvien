from database import Base
from sqlalchemy import Column, Integer, String,ForeignKey

class sinhvien(Base):
    __tablename__="sinhviens"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    email=Column(String)
    lop=Column(String)

class account(Base):
    __tablename__="accounts"
    id=Column(Integer,primary_key=True)
    username=Column(String)
    password=Column(String)

class RefreshToken(Base):
    __tablename__ = "refresh_tokens"
    id         = Column(Integer, primary_key=True)
    token      = Column(String, unique=True)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    expired_at = Column(String) 