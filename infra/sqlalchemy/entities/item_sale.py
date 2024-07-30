
from infra.sqlalchemy.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Float, DateTime, func
from sqlalchemy.orm import relationship



class ItemSaleEntity(Base):
        __tablename__ = 'sales_item'

        id = Column(Integer, primary_key= True, index=True, autoincrement=True)
        sale_id= Column(Integer, ForeignKey("sales.id"))
        product_id = Column(Integer, ForeignKey("products.id"))
        sale = relationship('SaleEntity')
        
        price = Column(Numeric(10, 2), nullable=False)  
        quantity = Column(Integer, nullable=False)
        created_at= Column(DateTime, insert_default=func.now())

        products = relationship("ProductEntity", back_populates="sales_items")
        sales = relationship("SaleEntity", back_populates="items")
 
        class Config:
                orm_mode = True
