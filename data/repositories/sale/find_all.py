from infra.sqlalchemy.entities.user import UserEntity

class FindAllRepository():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserEntity).all()
        return result