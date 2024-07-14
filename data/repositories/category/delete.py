from infra.sqlalchemy.database import SessionLocal
from infra.sqlalchemy.entities.user import UserEntity

class DeleteRepository():
    
    def delete_category(self, db_user: UserEntity):
        SessionLocal.delete(db_user)
        SessionLocal.commit()
