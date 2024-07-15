from typing import Optional
from pydantic import BaseModel, Field

from data.request.category.category import  CategoryRequest
from domain.category import CategoryModel

class ProductRequest(BaseModel):
    name: str
    description: str
    quantity: float
    price: float
    category_id: Optional[int]
    category: Optional[CategoryModel]