from typing import List
from fastapi import Depends
from data.repositories.user.find_all import FindAllRepository
from infra.sqlalchemy.database import SessionLocal, get_db
from domain.user import UserModel as UserDomain

class FindAllUseCase():

    def find_all(self) -> List[UserDomain]:
        db = SessionLocal
        _list = FindAllRepository(db).get_users()
        return _list