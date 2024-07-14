from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.category import CategoryEntity

class DeleteRepository():
    
    def delete_category(self, db_category: CategoryEntity):
        SessionLocal.delete(db_category)
        SessionLocal.commit()
