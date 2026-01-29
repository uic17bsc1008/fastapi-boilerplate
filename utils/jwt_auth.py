from fastapi import HTTPException, status, Depends
from datetime import datetime, timedelta, timezone
import jwt
from utils.env_config import getSettings
from typing import Union, Annotated
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.jwtoken import TokenData
from sqlalchemy.orm import Session
from database import get_db
from models.user import User




settings = getSettings()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")



def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Annotated[Session, Depends(get_db)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        email = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception
    return user