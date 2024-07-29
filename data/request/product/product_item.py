from typing import Optional
from pydantic import BaseModel, Field

from data.request.category.category import  CategoryRequest
from domain.category import CategoryModel

class ProductItemRequest(BaseModel):

    product_id: str
    description: str
    quantity: int
    price: float
    category_id: Optional[int] 
