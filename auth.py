from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

pwd_context=CryptContext(schemes=["bcrypt"])

#hash password
def hash_password(pwd:str):
    return pwd_context.hash(pwd)

#verify password
def verify_password(pwd:str,hashed_pwd:str):
    return pwd_context.verify(pwd,hashed_pwd)
secretkey="20112007"
algorithm="HS256"
def create_token(data:dict):
    to_encode=data.copy()
    to_encode["exp"]=datetime.utcnow()+timedelta(minutes=30)
    return jwt.encode(to_encode,secretkey,algorithm=algorithm)
def verify_token(token:str):
    try:
        payload=jwt.decode(token,secretkey,algorithms=[algorithm])
        return payload 
    except:
        return None


