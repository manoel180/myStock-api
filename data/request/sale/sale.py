
from typing import List, Optional
from pydantic import BaseModel, Field


from data.request.product.product_item import ProductItemRequest
from infra.sqlalchemy.entities.type_user import TypeUserEnum

class SaleRequest(BaseModel):
    login: str
    client_id : str
    amount: str
    items: Optional[List[ProductItemRequest]] 