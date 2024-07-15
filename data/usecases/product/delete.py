from data.repositories.product.delete import DeleteRepository
from data.repositories.product.find_id import FindByIdRepository


class DeleteUseCase():

    def delete(self, id: int):
        
        obj_db = FindByIdRepository().product_by_id(id)
        if (obj_db):
            DeleteRepository().delete_product(obj_db)
        return {"product deleted": obj_db.name}