from fastapi import APIRouter, Depends
from schemas.product import Product as schemaProduct
from models.product import Product
from sqlalchemy.orm import Session
from database import get_db

router =  APIRouter(prefix='/products',  tags=['Products'])

@router.post('/')
async def create_product(request:schemaProduct, db:Session = Depends(get_db)):
    new_product = Product(product_name=request.product_name, price=request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.get('/')
async def get_products(db:Session = Depends(get_db)):
    all_products = db.query(Product).all()
    return all_products