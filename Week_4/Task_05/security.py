import os
import json

import jwt
import bcrypt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Optional

from dotenv import load_dotenv


load_dotenv()
USERS = os.getenv("USERS")
SECRET_KEY = "my_super_secret_key"
ALGORITHM = "HS256"
STATIC_SALT = b'$2b$12$N6gO..ByM9lfx4Ua5jWqp.'
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__truncate_error=True)


def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, STATIC_SALT)

    return hashed.decode('utf-8')


def verify_user(username: str, hashed_password: str) -> bool:
    with open(USERS, "r") as f:
        data = json.load(f)

    for i in data:
        if i["username"] == username and i["hashed_password"] == hashed_password:
            return True

    return False


def verify_token(token: str) -> bool:
    payload = decode_access_token(token)
    try:
        if not payload["ok"]:
            return False
    except KeyError:
        return verify_user(payload["username"], payload["hashed_password"])

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {"ok": False, "description": "token is expired"}
    except jwt.PyJWTError:
        return {"ok": False, "description": "some error with token occured"}
