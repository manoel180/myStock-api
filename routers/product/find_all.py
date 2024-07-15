from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated, List

from fastapi.responses import JSONResponse
from data.usecases.product.find_all import FindAllUseCase
from domain.product import ProductModel
from main import oauth2_scheme


router = APIRouter()

# Get records from the users table
@router.get('/product', tags=['Product'], response_model=List[ProductModel], status_code=200)
def find_all(token: Annotated[str, Depends(oauth2_scheme)]) -> List[ProductModel]:
    
    result = FindAllUseCase().find_all()
    if(not result):
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return result