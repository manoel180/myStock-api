from data.repositories.category.delete import DeleteRepository
from data.repositories.category.find_id import FindByIdRepository


class DeleteUseCase():

    def delete(self, id: int):
        
        obj_db = FindByIdRepository().category_by_id(id)
        if (obj_db):
            DeleteRepository().delete_category(obj_db)
        return {"category deleted": obj_db.name}