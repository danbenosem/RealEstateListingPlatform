from Dtos.requests import RegisterUserRequest,LoginUserRequest,LogOutUserRequest
from models.user import User
from utils.mapper import UserMapper
from Dtos.responses import RegisterResponse,LoginUserResponse,LogoutUserResponse
from sqlalchemy.exc import IntegrityError


class AuthenticationService:

    def __init__(self,repository):
        self.repository = repository

    def register_user(self,request:RegisterUserRequest):
        user = UserMapper.user_mapper(request)
        try:
            self.repository.save(user)
            return RegisterResponse(success=True, message="registration successful")
        except IntegrityError:
            return RegisterResponse(success=False, message="user already exists")

    def login_user(self, request:LoginUserRequest):
        login_user = UserMapper.login_mapper(request)
        user = self.repository.find_by_email(login_user.email)
        if user is None:
            return LoginUserResponse(success=False, message="not registered")

        if user.password != login_user.password:
            return LoginUserResponse(success=False, message="wrong password")

        return LoginUserResponse(success=True, message="login successful", buyer_id=user.id)

    def logout_user(self, request: LogOutUserRequest):
        user = self.repository.find_by_email(request.email)
        if user is None:
            return LogoutUserResponse(success=False, message="user not found")

        return LogoutUserResponse(success=True, message="logout successful")