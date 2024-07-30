from infra.sqlalchemy.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Enum, Integer, String, Float, DateTime

from infra.sqlalchemy.entities.type_user import TypeUserEnum

class UserEntity(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key= True, index=True, autoincrement=True)
        name = Column(String(200))
        login = Column(String(50), unique=True)
        password = Column(String(120))
        type_user = Column(Enum(TypeUserEnum), 
                       default=(TypeUserEnum.CLIENT.value), nullable=False) 
        
        sales = relationship("SaleEntity", back_populates="client")
        products = relationship("ProductEntity", back_populates="seller")
        class Config:
                orm_mode = True