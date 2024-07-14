from data.repositories.category.find_id import FindByIdRepository
from data.repositories.category.save import SaveRepository
from data.request.category.category import CategoryRequest
from domain.category import CategoryModel


class UpdateUseCase():

    def update(self, id: int, _request: CategoryRequest) -> CategoryModel:
       
        obj_db = FindByIdRepository().category_by_id(id)
        if (obj_db):
             for key, value in _request.model_dump().items():
                 setattr(obj_db, key, value) if value else None              
        result = SaveRepository().save_category(obj_db)
        return result