from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from data.dto.token import TokenSchema
from data.usecases.auth.security import create_access_token, create_refresh_token


auth_router = APIRouter()

@auth_router.post('/login', tags= ['Auth'], summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = form_data.username
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    result = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    return result 
    # hashed_pass = user['password']
    # if not verify_password(form_data.password, hashed_pass):
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Incorrect email or password"
    #     )
    