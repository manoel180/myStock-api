from data.repositories.user.find_login import FindByLoginRepository
from data.request.auth.login import LoginRequest
from infra.sqlalchemy.database import SessionLocal
from domain.user import UserModel as UserDomain
from data.usecases.auth.security import create_access_token, create_refresh_token

from passlib.hash import pbkdf2_sha256
class LoginUseCase():

    def login(self, user_request: LoginRequest) -> UserDomain:
        user = self.find_user(user_request.login)
        result = ''
        if user is not None and pbkdf2_sha256.verify(user_request.password, user.password):
            access_token = create_access_token(user)
            refresh_token = create_refresh_token(user)
            result = {"access_token": access_token, 
                      "refresh_token": refresh_token
                    }
        return result
    
    def find_user(self, login: str) -> UserDomain:
        
        return FindByLoginRepository().user_by_login(login)