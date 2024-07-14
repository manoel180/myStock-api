from typing import List
from fastapi import Depends
from data.repositories.user.find_id import FindByIdRepository
from data.repositories.user.save import SaveRepository
from data.request.user.user import UserRequest
from infra.sqlalchemy.database import SessionLocal, get_db
from domain.user import UserModel as UserDomain

from passlib.hash import pbkdf2_sha256
from infra.sqlalchemy.entities.user import UserEntity


class UpdateUseCase():

    def update(self, id_user: int, user_request: UserRequest) -> UserDomain:
        db = SessionLocal

        user_db = FindByIdRepository(db).user_by_id(id_user)
        if (user_db):
            user_db.name = user_request.name
            user_db.login = user_request.login
            if(not pbkdf2_sha256.verify(user_request.password, user_db.password)):
                user_db.password = pbkdf2_sha256.hash(user_request.password)
            # for key, value in user_request.model_dump().items():
            #     setattr(user_db, key, value) if value else None
                                
        result = SaveRepository(db).save_user(user_db)
        return result