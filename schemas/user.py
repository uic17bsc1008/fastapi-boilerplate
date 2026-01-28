from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    name : str = Field(..., max_length=30)
    email : EmailStr
    password : str = Field(..., min_length=6, max_length=30)