
from infra.sqlalchemy.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, func
from sqlalchemy.orm import relationship



class ItemSaleEntity(Base):
        __tablename__ = 'sales_item'

        id = Column(Integer, primary_key= True, index=True, autoincrement=True)
        product_id = Column(Integer, ForeignKey("products.id"))
        sale = relationship('SaleEntity')
        seller= relationship('UserEntity')
        created_at= Column(DateTime, insert_default=func.now())

        product = relationship("ProductEntity", back_populates="product")
 
        class Config:
                orm_mode = True
