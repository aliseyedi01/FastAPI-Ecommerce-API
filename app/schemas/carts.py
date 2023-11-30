from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Base Config
class BaseConfig:
    orm_mode = True


class ProductBase(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: int
    discount_percentage: float
    rating: float
    stock: int
    brand: str
    thumbnail: str
    images: List[str]
    is_published: bool
    created_at: datetime
    category_id: int

    class Config(BaseConfig):
        pass


# Base Cart & Cart_Item
class CartItemBase(BaseModel):
    id: int
    product_id: int
    quantity: int
    subtotal: int
    product: ProductBase


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

    class Config(BaseConfig):
        pass


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
