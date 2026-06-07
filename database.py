from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()  # đọc file .env

engine = create_engine(
    f"postgresql://postgres:duc20112007@localhost/sinhvien_db"
)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass