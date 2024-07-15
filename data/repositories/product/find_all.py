from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.product import ProductEntity

class FindAllRepository():
    
    

    def get_products(self):
        result = SessionLocal.query(ProductEntity).all()
        return result