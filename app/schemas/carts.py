from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from app.schemas.products import ProductBase, CategoryBase


# Base Config
class BaseConfig:
    from_attributes = True


class ProductBaseCart(ProductBase):
    category: CategoryBase = Field(exclude=True)

    class Config(BaseConfig):
        pass


# Base Cart & Cart_Item
class CartItemBase(BaseModel):
    id: int
    product_id: int
    quantity: int
    subtotal: float
    product: ProductBaseCart


class CartBase(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    total_amount: float
    cart_items: List[CartItemBase]

    class Config(BaseConfig):
        pass


class CartOutBase(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    total_amount: float
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
    cart_items: List[CartItemCreate]

    class Config(BaseConfig):
        pass


# Update Cart
class CartUpdate(CartCreate):
    pass
