# schemas.py
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
