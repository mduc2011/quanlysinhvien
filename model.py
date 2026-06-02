from database import Base
from sqlalchemy import Column, Integer, String

class sinhvien(Base):
    __tablename__="sinhvien"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    email=Column(String)
    lop=Column(String)

class account(Base):
    __tablename__="account"
    id=Column(Integer,primary_key=True)
    username=Column(String)
    password=Column(String)

    