from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    id: int
    name: str


class ProductBase(BaseModel):
    id: int
    title: str
    description: str
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
    category: CategoryBase

    class Config:
        orm_mode = True


class ProductCreate(BaseModel):
    title: str
    description: str
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

    class Config:
        orm_mode = True


class ProductOut(BaseModel):
    message: str
    product: ProductBase

    class Config:
        orm_mode = True


class ProductsOut(BaseModel):
    message: str
    products: List[ProductBase]

    class Config:
        orm_mode = True


class ProductOutDelete(BaseModel):
    message: str
    product: ProductBase

    class config:
        fields = {'category': {'exclude': True}}
