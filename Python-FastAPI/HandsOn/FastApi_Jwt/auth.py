from datetime import datetime,timedelta,timezone
import jwt
from pwdlib import PasswordHash
SECRET_KEY = "change-this-secret-key-in-production"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 15

REFRESH_TOKEN_EXPIRE_DAYS = 7

password_hash = PasswordHash.recommended()
def hash_password(password:str)->str:
    return password_hash.hash(password)
def verify_password(plain_password:str,
                    hash_password:str)->bool:
    return password_hash.verify(plain_password,hash_password)
def create_access_token(username:str,role:str)->str:
    expire=(datetime.now(timezone.utc)+
    timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    payload={
        'sub':username,
        'role':role,
        'type':'access',
        'exp':expire
    }
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
def create_refresh_token(
    username:str
)->str:
     expire = (
        datetime.now(timezone.utc)
        + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    )
     payload = {
        "sub": username,
        "type": "refresh",
        "exp": expire
    }
     return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
def decode_token(token:str)->dict:
    return jwt.decode(token,
                      SECRET_KEY,
                      algorithms=[ALGORITHM])