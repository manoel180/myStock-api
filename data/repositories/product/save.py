from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.product import ProductEntity

class SaveRepository():
    
    def save_product(self, product_entity: ProductEntity):
        SessionLocal.add(product_entity)
        SessionLocal.commit()
        SessionLocal.refresh(product_entity)
        return product_entity