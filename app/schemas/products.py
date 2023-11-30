from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    id: int
    name: str


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
    category: CategoryBase

    class Config(BaseConfig):
        pass


class ProductCreate(ProductBase):
    id: int = Field(exclude=True)
    category: CategoryBase = Field(exclude=True)

    class Config(BaseConfig):
        pass


class ProductUpdate(ProductCreate):
    pass


class ProductOut(BaseModel):
    message: str
    data: ProductBase

    class Config(BaseConfig):
        pass


class ProductsOut(BaseModel):
    message: str
    data: List[ProductBase]

    class Config(BaseConfig):
        pass


class ProductDelete(ProductBase):
    category: CategoryBase = Field(exclude=True)


class ProductOutDelete(BaseModel):
    message: str
    data: ProductDelete
