from typing import Annotated
from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from data.dto.token import TokenSchema
from data.request.auth.login import LoginRequest
from data.usecases.auth.login import LoginUseCase

auth_router = APIRouter()

@auth_router.post('/login', tags= ['Auth'], summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = form_data.username
    password = form_data.password

    if user is None or password is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    else:
        login_request= LoginRequest(login=user, password=password)
        result = LoginUseCase().login(login_request)
    if result == '': 
        return JSONResponse(status_code=404, content={'message': "Incorrect email or password"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

    