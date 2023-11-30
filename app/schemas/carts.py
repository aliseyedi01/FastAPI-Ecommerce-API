from pydantic import BaseModel
from typing import List
from datetime import datetime


class CartItemBase(BaseModel):
    id: int
    product_id: int
    quantity: int
    subtotal: int


class BaseConfig:
    orm_mode = True


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


class CartOut(BaseModel):
    message: str
    data: CartBase

    class Config(BaseConfig):
        pass


class CartsOutList(BaseModel):
    message: str
    data: List[CartBase]


class CartOutDelete(BaseModel):
    message: str
    data: CartOutBase


class CartCreate(BaseModel):
    user_id: int
    created_at: datetime
    total_amount: int
    cart_items: List[CartItemBase]

    class Config(BaseConfig):
        pass


class CartUpdate(BaseModel):
    user_id: int
    items: List[CartItemBase]
