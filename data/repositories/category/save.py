from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.category import CategoryEntity

class SaveRepository():
    
    def save_category(self, category_entity: CategoryEntity):
        SessionLocal.add(category_entity)
        SessionLocal.commit()
        SessionLocal.refresh(category_entity)
        return category_entity