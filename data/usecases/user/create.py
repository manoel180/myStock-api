from typing import List
from fastapi import Depends
from data.repositories.user.save import SaveRepository
from data.request.user.user import UserRequest
from infra.sqlalchemy.database import SessionLocal, get_db
from domain.user import UserModel as UserDomain

from passlib.hash import pbkdf2_sha256
from infra.sqlalchemy.entities.user import UserEntity


class CreateUseCase():

    def create(self, user_request: UserRequest) -> UserDomain:
        db = SessionLocal
        user_request.password = pbkdf2_sha256.hash(user_request.password)
        user_in_db = UserEntity(**user_request.model_dump())
        result = SaveRepository(db).save_user(user_in_db)
        return result