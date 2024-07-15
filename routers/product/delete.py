from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import Optional, List

from fastapi.encoders import jsonable_encoder
from data.usecases.product.delete import DeleteUseCase
from domain.product import ProductModel


router = APIRouter()

# Delete user from the users table
@router.delete('/product/{id}', tags=['Product'], response_model=ProductModel, status_code=200)
def delete(id: int):
   
    result = DeleteUseCase().delete(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))