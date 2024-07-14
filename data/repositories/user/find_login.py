from infra.sqlalchemy.entities.user import UserEntity

class FindByLoginRepository():
    
    def __init__(self, db) -> None:
        self.db = db

    def user_by_login(self, login):
        result = self.db.query(UserEntity).filter(UserEntity.login == login).first()
        return result