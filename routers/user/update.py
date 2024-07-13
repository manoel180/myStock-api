from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import Optional, List
from data.request.user.user import UserRequest
# from data.userService import UserService

from fastapi.encoders import jsonable_encoder


user_router = APIRouter()

# Get records from the users table
@user_router.put('/users/{id}', tags=['Users'],  status_code=200)
def update(id: int, user: UserRequest):
    # db = Session()
    # result = UserService(db).get_users()
    result = {"message": "Item replaced", "id": id, **user.model_dump()}
    # if not result:
        # return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))