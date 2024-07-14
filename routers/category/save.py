from fastapi import APIRouter
from fastapi.responses import JSONResponse
from data.request.category.category import CategoryRequest
from fastapi.encoders import jsonable_encoder
from data.usecases.category.create import CreateUseCase
from domain.category import CategoryModel


router = APIRouter()

# Get records from the users table
@router.post('/category', tags=['Category'], response_model=CategoryModel, status_code=200)
def save(_request: CategoryRequest):

    result = CreateUseCase().create(_request)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return _request