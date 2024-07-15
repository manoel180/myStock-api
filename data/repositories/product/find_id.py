from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.product import ProductEntity

class FindByIdRepository():
    
    def product_by_id(self, id):
        result = SessionLocal.get(ProductEntity, id)
        return result