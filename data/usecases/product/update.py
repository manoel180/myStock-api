from data.repositories.product.find_id import FindByIdRepository
from data.repositories.product.save import SaveRepository
from data.request.product.product import ProductRequest
from domain.product import ProductModel
from infra.sqlalchemy.entities.product import ProductEntity


class UpdateUseCase():

    def update(self, id: int, _request: ProductRequest) -> ProductModel:
        
        obj_db = FindByIdRepository().product_by_id(id)
        if (obj_db):  
             for key, value in _request.model_dump(exclude='category').items():
                 setattr(obj_db, key, value) if value else None              
        result = SaveRepository().save_product(obj_db)
        return result