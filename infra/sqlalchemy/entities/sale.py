
from infra.sqlalchemy.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, DateTime, func
from sqlalchemy.orm import relationship



class SaleEntity(Base):
        __tablename__ = 'sales'

        id = Column(Integer, primary_key= True, index=True, autoincrement=True)
        client_id = Column(Integer, ForeignKey("users.id"))
        
        amount = Column(Numeric(10, 2), nullable=False)
        observation = Column(String(500), nullable=True)
        created_at= Column(DateTime, insert_default=func.now())

        items = relationship("ItemSaleEntity", back_populates="sales")
        client= relationship('UserEntity', back_populates="sales")
       
        class Config:
                orm_mode = True
