from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated, List
from data.usecases.user.find_all import FindAllUseCase
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