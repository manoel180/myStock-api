from infra.sqlalchemy.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime

class UserEntity(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key= True, index=True)
        name = Column(String(200))
        login = Column(String(50), unique=True)
        password = Column(String(50), unique=True)
