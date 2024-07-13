from pydantic import BaseModel, Field
from typing import Optional, List


class UserModel(BaseModel):
    id: int
    username: str