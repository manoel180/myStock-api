from typing import Optional
from pydantic import BaseModel, Field

class CategoryRequest(BaseModel):
    id: Optional[int]
    name: str
    description: str