from fastapi import APIRouter
from fastapi.responses import JSONResponse
from data.request.user.user import UserRequest

from fastapi.encoders import jsonable_encoder
from data.usecases.user.update import UpdateUseCase
from domain.user import UserModel

user_router = APIRouter()

# Get records from the users table
@user_router.put('/users/{id}', tags=['Users'], response_model=UserModel,  status_code=200)
def update(id: int, user: UserRequest):
    result = UpdateUseCase().update(id, user_request=user)
   
    if result == '':
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return result