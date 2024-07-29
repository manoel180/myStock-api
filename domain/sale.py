from pydantic import BaseModel, Field
from typing import Optional, List


from domain.product import ProductModel
from domain.user import UserModel
from infra.sqlalchemy.entities.type_user import TypeUserEnum


class SaleModel(BaseModel):
    id: int
    client: UserModel

    amount: float
    observation: Optional[str] 
    created_at: Optional[TypeUserEnum] 

    items: List[ProductModel]