from pydantic import BaseModel, Field
from typing import Optional, List

class CategoryModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]