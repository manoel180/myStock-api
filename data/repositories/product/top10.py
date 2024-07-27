from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.product import ProductEntity

class Top10Repository():
    
    

    def get_products(self):
        result = SessionLocal.query(ProductEntity).order_by().limit(4).all()
        return result