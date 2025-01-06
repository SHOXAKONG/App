from typing import Optional
from pydantic import BaseModel, validator

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int

    @validator("price")
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")
        return value

    @validator("stock")
    def validate_stock(cls, value):
        if value < 0:
            raise ValueError("Stock cannot be negative")
        return value

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    customer_id: int

class Order(OrderBase):
    id: int
    status: str

    class Config:
        orm_mode = True


