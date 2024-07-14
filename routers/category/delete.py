from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from data.usecases.category.delete import DeleteUseCase
from domain.category import CategoryModel


router = APIRouter()

# Delete user from the users table
@router.delete('/category/{id}', tags=['Category'], response_model=CategoryModel, status_code=200)
def delete(id: int):
   
    result = DeleteUseCase().delete(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))