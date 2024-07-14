from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    login: str
    password: str