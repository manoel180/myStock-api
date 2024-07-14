from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.category import CategoryEntity

class FindByIdRepository():
    
    def category_by_id(self, id):
        result = SessionLocal.get(CategoryEntity, id)
        return result