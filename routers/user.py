from fastapi import APIRouter, Depends
from schemas.user import User as schemaUser
from models.user import User
from sqlalchemy.orm import Session
from database import get_db
from utils.hashing import Hash

router =  APIRouter(prefix='/users', tags=['Users'])

@router.post('/')
async def create_user(request:schemaUser, db:Session = Depends(get_db)):
    new_user = User(name=request.name, email=request.email, password=Hash.make(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/')
async def get_users(db:Session = Depends(get_db)):
    all_users = db.query(User).all()
    return all_users