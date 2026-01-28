from pydantic import BaseModel, Field

class Product(BaseModel):
    product_name : str = Field(..., max_length=50)
    price : float = Field(...)