from typing import List
from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    id: int
    name: str


class CategoryCreate(BaseModel):
    name: str


class CategoryUpdate(BaseModel):
    name: str


class CategoryOut(BaseModel):
    message: str
    data: CategoryBase


class CategoriesOut(BaseModel):
    message: str
    data: List[CategoryBase]


class CategoryDelete(BaseModel):
    id: int
    name: str


class CategoryOutDelete(BaseModel):
    message: str
    data: CategoryDelete
