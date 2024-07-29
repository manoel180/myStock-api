from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from data.request.sale.sale import SaleRequest
from data.usecases.sale.make_sale import MakeSaleUseCase
from domain.sale import SaleModel


router = APIRouter()

# Get records from the products table
@router.post('/sale', tags=['Sale'], response_model=SaleModel, status_code=200)
def make_sale(_request: SaleRequest):

    result = MakeSaleUseCase().make_sale(_request)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(_request))