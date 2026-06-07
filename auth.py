from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
secretkey=os.getenv('secretkey')
algorithm=os.getenv('algorithm')

pwd_context=CryptContext(schemes=["bcrypt"])

#hash password
def hash_password(pwd:str):
    return pwd_context.hash(pwd)

#verify password
def verify_password(pwd:str,hashed_pwd:str):
    return pwd_context.verify(pwd,hashed_pwd)

def create_access_token(data:dict):
    to_encode=data.copy()
    to_encode["exp"]=datetime.utcnow()+timedelta(seconds=30)
    return jwt.encode(to_encode,secretkey,algorithm=algorithm)

def create_refresh_token(data:dict):
    to_encode=data.copy()
    to_encode["exp"]=datetime.utcnow()+timedelta(minutes=5)
    return jwt.encode(to_encode,secretkey,algorithm=algorithm)

def verify_token(token:str):
    try:
        payload=jwt.decode(token,secretkey,algorithms=[algorithm])
        return payload 
    except:
        return None


