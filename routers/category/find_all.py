from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated, List

from fastapi.responses import JSONResponse
from data.usecases.category.find_all import FindAllUseCase
from domain.category import CategoryModel
from main import oauth2_scheme

router = APIRouter()



# Get records from the users table
@router.get('/category', tags=['Category'], response_model=List[CategoryModel], status_code=200)
def find_all(token: Annotated[str, Depends(oauth2_scheme)]) -> List[CategoryModel]:
    
    result = FindAllUseCase().find_all()
    if(not result):
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return result