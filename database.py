from sqlalchemy import create_engine, true;
from sqlalchemy.orm import sessionmaker,DeclarativeBase

engine=create_engine("sqlite:///sinhviens.db")

SessionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
