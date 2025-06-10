from pydantic import BaseModel, Field
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    price: float
    in_stock: bool = True

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True 