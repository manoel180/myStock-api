from pydantic import BaseModel, Field
from typing import Optional, List


class CategoryModel(BaseModel):
    name: str
    description: str