from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from schemas.product import Product as schemaProduct
from models.product import Product
from sqlalchemy.orm import Session
from database import get_db
from typing import Annotated
from schemas.user import User as schemaUser
from utils.jwt_auth import get_current_user


router =  APIRouter(prefix='/products',  tags=['Products'])

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_product(request:schemaProduct, db: Annotated[Session, Depends(get_db)], current_user: Annotated[schemaUser, Depends(get_current_user)]):
    new_product = Product(product_name=request.product_name, price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return JSONResponse({'detail':f"Product {new_product.product_name} has been created successfully!"})

@router.get('/', status_code=status.HTTP_200_OK)
async def get_products(db: Annotated[Session, Depends(get_db)], current_user: Annotated[schemaUser, Depends(get_current_user)]):
    all_products = db.query(Product).all()
    if not all_products:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found!")
    return all_products