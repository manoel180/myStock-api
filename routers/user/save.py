from fastapi import APIRouter
from fastapi.responses import JSONResponse
from data.request.user.user import UserRequest
# from data.userService import UserService
from fastapi.encoders import jsonable_encoder
from domain.user import UserModel as UserDomain


user_router = APIRouter()

# Get records from the users table
@user_router.post('/users', tags=['Users'], response_model=UserDomain, status_code=200)
def save(userRequest: UserRequest):
    # db = Session()
    # result = UserService(db).get_users()
    # if not result:
        # return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(userRequest))