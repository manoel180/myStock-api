from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import Optional, List

# from data.userService import UserService
# from infra.database.entities.user import UserEntity as UserModel
from fastapi.encoders import jsonable_encoder
from data.usecases.user.delete import DeleteUseCase
from domain.user import UserModel as UserDomain


user_router = APIRouter()

# Delete user from the users table
@user_router.delete('/users/{id}', tags=['Users'], response_model=UserDomain, status_code=200)
def delete(id: int):
   
    result = DeleteUseCase().delete(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))