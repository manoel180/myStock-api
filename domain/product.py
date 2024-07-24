from pydantic import BaseModel, Field
from typing import Optional, List

from domain.category import CategoryModel


class ProductModel(BaseModel):
    id: int
    name: str
    description: str
    quantity: int
    quantity_alert: Optional[int]
    price: float
    category_id: int 
    category: Optional[CategoryModel]