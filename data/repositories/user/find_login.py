from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.user import UserEntity

class FindByLoginRepository():
    
    def user_by_login(self, login):
        result = SessionLocal.query(UserEntity).filter(UserEntity.login == login).first()
        return result