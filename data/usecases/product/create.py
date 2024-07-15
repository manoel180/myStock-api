from data.repositories.product.save import SaveRepository
from data.request.product.product import ProductRequest
from domain.product import ProductModel
from infra.sqlalchemy.entities.category import ProductEntity


class CreateUseCase():

    def create(self, product_request: ProductRequest) -> ProductModel:
        
        obj = ProductEntity(**product_request.model_dump(exclude='category'))
        result = SaveRepository().save_product(obj)
        return result