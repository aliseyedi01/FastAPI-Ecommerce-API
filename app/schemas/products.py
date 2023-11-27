from datetime import datetime
from typing import List

from pydantic import BaseModel, Field
from uuid import UUID


class CategoryBase(BaseModel):
    id: UUID
    name: str


class ProductBase(BaseModel):
    id: UUID
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
        # exclude = ['id']


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
