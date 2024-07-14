from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.category import CategoryEntity

class FindAllRepository():
    
    

    def get_categories(self):
        result = SessionLocal.query(CategoryEntity).all()
        return result