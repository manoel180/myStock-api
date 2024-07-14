from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    login: str
    name: str
    password: str