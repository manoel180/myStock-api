from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.product import ProductEntity

class DeleteRepository():
    
    def delete_product(self, db_product: ProductEntity):
        SessionLocal.delete(db_product)
        SessionLocal.commit()
