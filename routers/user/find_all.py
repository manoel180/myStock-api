from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi.security import OAuth2PasswordBearer
from data.usecases.user.find_all import FindAllUseCase
from infra.sqlalchemy.database import get_db, SessionLocal
from data.repositories.user.find_all import FindAllRepository
from fastapi.encoders import jsonable_encoder
from domain.user import UserModel as UserDomain

user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/api/login")

# Get records from the users table
@user_router.get('/users', tags=['Users'], response_model=List[UserDomain], status_code=200)
def find_all(token: Annotated[str, Depends(oauth2_scheme)]) -> List[UserDomain]:
    
    result = FindAllUseCase().find_all()
    if not result: 
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))