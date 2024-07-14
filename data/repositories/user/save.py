from infra.sqlalchemy.entities.user import UserEntity

class SaveRepository():
    
    def __init__(self, db) -> None:
        self.db = db

    def save_user(self, user_entity: UserEntity):
        self.db.add(user_entity)
        self.db.commit()
        self.db.refresh(user_entity)
        return user_entity