from infra.sqlalchemy.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship



class ProductEntity(Base):
        __tablename__ = 'products'

        id = Column(Integer, primary_key= True, index=True, autoincrement=True)
        name = Column(String(200), nullable=False, unique=True)
        description = Column(String(350))
        quantity = Column(Integer)
        quantity_alert = Column(Integer, default=0)
        price = Column(Float, nullable=False)
        category_id = Column(Integer, ForeignKey("categories.id"))
        category = relationship('CategoryEntity', back_populates="products")

        class Config:
                orm_mode = True
