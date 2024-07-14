from infra.sqlalchemy.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime

class CategoryEntity(Base):
        __tablename__ = 'categories'

        id = Column(Integer, primary_key= True, index=True, autoincrement=True)
        name = Column(String(200), nullable=False, unique=True)
        description = Column(String(350))
        

        class Config:
                orm_mode = True