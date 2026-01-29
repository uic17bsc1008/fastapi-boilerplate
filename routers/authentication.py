from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.auth import Login as schemaLogin
from schemas.jwtoken import Token
from typing import Annotated
from database import  get_db
from sqlalchemy.orm import Session
from models.user import User
from utils.hashing import Hash
from utils.jwt_auth import create_access_token
from utils.env_config import getSettings
from fastapi.security import OAuth2PasswordRequestForm




settings = getSettings()


router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/login')
async def user_login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(get_db)]):
    user = db.query(User).filter(User.email == request.username).first()
    if not user or not Hash.check(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires,)
    return Token(access_token=access_token, token_type="bearer",)
    
    

