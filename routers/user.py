from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from schemas.user import User as schemaUser
from models.user import User
from sqlalchemy.orm import Session
from database import get_db
from utils.hashing import Hash
from typing import Annotated

router =  APIRouter(prefix='/users', tags=['Users'])

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(request:schemaUser, db: Annotated[Session, Depends(get_db)]):
    new_user = User(name=request.name, email=request.email, password=Hash.make(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse({'detail':f"User {new_user.name} has been created successfully!"})


@router.get('/{id}', status_code=status.HTTP_200_OK)
async def get_user(id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist!")
    return user


@router.get('/', status_code=status.HTTP_200_OK)
async def get_users(db: Annotated[Session, Depends(get_db)]):
    all_users = db.query(User).all()
    if not all_users:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found!")
    return all_users