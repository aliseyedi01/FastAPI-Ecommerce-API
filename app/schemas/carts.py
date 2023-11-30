from pydantic import BaseModel
from typing import List
from datetime import datetime


# Base Config
class BaseConfig:
    orm_mode = True


# Base Cart & Cart_Item
class CartItemBase(BaseModel):
    id: int
    product_id: int
    quantity: int
    subtotal: int


class CartBase(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    total_amount: int
    cart_items: List[CartItemBase]

    class Config(BaseConfig):
        pass


class CartOutBase(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    total_amount: int
    cart_items: List[CartItemBase]

    class Config(BaseConfig):
        pass


# Get Cart
class CartOut(BaseModel):
    message: str
    data: CartBase

    class Config(BaseConfig):
        pass


class CartsOutList(BaseModel):
    message: str
    data: List[CartBase]


class CartsUserOutList(BaseModel):
    message: str
    data: List[CartBase]

# Delete Cart


class CartOutDelete(BaseModel):
    message: str
    data: CartOutBase


# Create Cart
class CartItemCreate(BaseModel):
    product_id: int
    quantity: int


class CartCreate(BaseModel):
    user_id: int
    cart_items: List[CartItemCreate]

    class Config(BaseConfig):
        pass


# Update Cart
class CartUpdate(BaseModel):
    user_id: int
    items: List[CartItemBase]
