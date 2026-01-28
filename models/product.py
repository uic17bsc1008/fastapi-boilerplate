from sqlalchemy import Column, Integer, String, Float
from models.base import Model


class Product(Model):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_name = Column(String(30), nullable=False)
    price = Column(Float, nullable=False)