from fastapi import APIRouter
from fastapi.responses import JSONResponse
from data.request.product.product import ProductRequest
from fastapi.encoders import jsonable_encoder
from data.usecases.product.create import CreateUseCase
from domain.product import ProductModel


router = APIRouter()

# Get records from the products table
@router.post('/product', tags=['Product'], response_model=ProductModel, status_code=200)
def save(_request: ProductRequest):

    result = CreateUseCase().create(_request)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return _request