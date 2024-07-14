from typing import List
from fastapi import Depends
from data.repositories.user.delete import DeleteRepository
from data.repositories.user.find_id import FindByIdRepository
from data.repositories.user.save import SaveRepository
from data.request.user.user import UserRequest
from infra.sqlalchemy.database import SessionLocal, get_db
from domain.user import UserModel as UserDomain

from passlib.hash import pbkdf2_sha256
from infra.sqlalchemy.entities.user import UserEntity


class DeleteUseCase():

    def delete(self, id_user: int):
        
        user_db = FindByIdRepository().user_by_id(id_user)
        if (user_db):
            DeleteRepository().delete_user(user_db)
        return {"user deleted": user_db.name}