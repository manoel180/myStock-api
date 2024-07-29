from data.repositories.sale.save import SaveRepository
from data.request.sale.sale import SaleRequest
from domain.sale import SaleModel

from infra.sqlalchemy.entities.sale import SaleEntity


class MakeSaleUseCase():

    def make_sale(self, sale_request: SaleRequest) -> SaleModel:
        sale_request
        user_in_db = SaleEntity(**sale_request.model_dump())
        result = SaveRepository().save_user(user_in_db)
        return result