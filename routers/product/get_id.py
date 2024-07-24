from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated

from fastapi.responses import JSONResponse
from data.usecases.product.find_id import FindIdUseCase
from domain.product import ProductModel
from main import oauth2_scheme


router = APIRouter()

# Get record from the product table
@router.get('/product/{id}', tags=['Product'], response_model=ProductModel, status_code=200)
def get_id(token: Annotated[str, Depends(oauth2_scheme)], id: int) -> ProductModel:
    
    result = FindIdUseCase().get_id(id)
    if(not result):
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return result