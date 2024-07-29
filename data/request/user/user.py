
from typing import Optional
from pydantic import BaseModel, Field

from infra.sqlalchemy.entities.type_user import TypeUserEnum

class UserRequest(BaseModel):
    login: str
    name: str
    password: str
    type: Optional[TypeUserEnum] 