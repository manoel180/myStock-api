from fastapi import APIRouter
from fastapi.responses import JSONResponse
from data.request.category.category import CategoryRequest
from data.usecases.category.update import UpdateUseCase
from domain.category import CategoryModel

router = APIRouter()

# Get records from the users table
@router.put('/category/{id}', tags=['Category'], response_model=CategoryModel,  status_code=200)
def update(id: int, _request: CategoryRequest):
    result = UpdateUseCase().update(id, _request)
    if result == '':
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return result