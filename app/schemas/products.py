from datetime import datetime
from typing import List

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: int
    title: str
    description: str
    price: int
    discount_percentage: float
    rating: float
    stock: int
    brand: str
    category: str
    thumbnail: str
    images: List[str]
    is_published: bool
    created_at: datetime


class ProductOut(BaseModel):
    message: str
    product: ProductBase

    class Config:
        orm_mode = True


class ProductsOut(BaseModel):
    message: str
    products: List[ProductBase]
