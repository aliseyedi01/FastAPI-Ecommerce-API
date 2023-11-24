from datetime import datetime

from pydantic import BaseModel


class ProductsOut(BaseModel):
    name: str
