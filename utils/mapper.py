from models.user import User
from Dtos.requests import RegisterUserRequest, LoginUserRequest, LogOutUserRequest


class UserMapper:
    @staticmethod
    def user_mapper(request:RegisterUserRequest):
        return Buyer(name=request.name,email=request.email,password=request.password)

    @staticmethod
    def login_mapper(request:LoginUserRequest):
        return Buyer(email=request.email,password=request.password)

    @staticmethod
    def logout_mapper(request:LogOutUserRequest):
        return



