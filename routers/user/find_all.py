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
from main import oauth2_scheme

user_router = APIRouter()



# Get records from the users table
@user_router.get('/users', tags=['Users'], response_model=List[UserDomain], status_code=200)
def find_all(token: Annotated[str, Depends(oauth2_scheme)]) -> List[UserDomain]:
    
    result = FindAllUseCase().find_all()
    return result
    # if not result: 
    #     return JSONResponse(status_code=404, content={'message': "Not found"})
    # return JSONResponse(status_code=200, content=jsonable_encoder(result))