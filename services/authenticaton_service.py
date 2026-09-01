from Dtos.requests import RegisterUserRequest,LoginUserRequest
from models.buyer import Buyer
from utils.mapper import UserMapper
from Dtos.responses import RegisterResponse,LoginUserResponse,LogoutUserResponse
from sqlalchemy.exc import IntegrityError


class AuthenticationService:

    def __init__(self,repository):
        self.repository = repository

    def register_user(self,request:RegisterUserRequest):
        buyer= UserMapper.user_mapper(request)
        try:
            self.repository.save(buyer)
            return  RegisterResponse(success=True, message="registration successful")
        except IntegrityError:
            return  RegisterResponse(success=False,message="user already exists")

    def login_user(self, request:LoginUserRequest):
        login_user=UserMapper.login_mapper(request)
        buyer= self.repository.find_by_email(login_user.email)
        if buyer is None:

            return LoginUserResponse(success=False,message="not registered")

        if buyer.password != login_user.password:
            return LoginUserResponse(success=False,message="wrong password")

        return  LoginUserResponse(success=True,message="login successful",buyer_id=buyer.id)


    def logout_user(self):










