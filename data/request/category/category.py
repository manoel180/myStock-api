from pydantic import BaseModel, Field

class CategoryRequest(BaseModel):
    name: str
    description: str