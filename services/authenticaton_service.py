from Dtos.requests import RegisterBuyerRequest,LoginBuyerRequest
from models.buyer import Buyer
from utils.mapper import UserMapper
from Dtos.responses import RegisterResponse,LoginResponse
from sqlalchemy.exc import IntegrityError


class AuthenticationService:

    def __init__(self,repository):
        self.repository = repository

    def register_buyer(self,request:RegisterBuyerRequest):
        buyer= UserMapper.buyer_mapper(request)
        try:
            self.repository.save(buyer)
            return  RegisterResponse(success=True, message="registration successful")
        except IntegrityError:
            return  RegisterResponse(success=False,message="user already exists")

    def login_buyer(self, request:LoginBuyerRequest):
        login_user=UserMapper.login_mapper(request)
        buyer= self.repository.find_by_email(login_user.email)
        if buyer is None:

            return LoginResponse(success=False,message="not registered")

        if buyer.password != login_user.password:
            return LoginResponse(success=False,message="wrong password")

        return  LoginResponse(success=True,message="login successful",buyer_id=buyer.id)












