from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.user import UserEntity

class FindByIdRepository():
    
    def user_by_id(self, id):
        result = SessionLocal.get(UserEntity, id)
        return result