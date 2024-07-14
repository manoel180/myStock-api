from data.repositories.category.save import SaveRepository
from data.request.category.category import CategoryRequest
from domain.category import CategoryModel
from infra.sqlalchemy.entities.category import CategoryEntity


class CreateUseCase():

    def create(self, category_request: CategoryRequest) -> CategoryModel:
        
        obj = CategoryEntity(**category_request.model_dump())
        result = SaveRepository().save_category(obj)
        return result