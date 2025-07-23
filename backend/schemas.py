from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime

class UserCreate(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: int
    email: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    stock: int

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    stock: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    product_ids: List[int]
    quantities: List[int]

class Order(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    order_items: List[dict] # Nested schema for order items

    class Config:
        orm_mode = True

class OrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

class ReviewCreate(BaseModel):
    product_id: int
    rating: int
    comment: Optional[str] = None

class Review(BaseModel):
    id: int
    product_id: int
    rating: int
    comment: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
