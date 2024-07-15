from fastapi import APIRouter
from fastapi.responses import JSONResponse
from data.request.product.product import ProductRequest
from data.usecases.product.update import UpdateUseCase
from domain.product import ProductModel

router = APIRouter()

# Get records from the users table
@router.put('/product/{id}', tags=['Product'], response_model=ProductModel,  status_code=200)
def update(id: int, _request: ProductRequest):
    result = UpdateUseCase().update(id, _request)
    if result == '':
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return result