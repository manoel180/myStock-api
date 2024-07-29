from pydantic import BaseModel, Field
from typing import Optional, List

from infra.sqlalchemy.entities.type_user import TypeUserEnum


class UserModel(BaseModel):
    id: int
    name: str
    login: str
    type: Optional[TypeUserEnum]