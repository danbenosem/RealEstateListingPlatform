from models.buyer import Buyer
from Dtos.requests import RegisterBuyerRequest, LoginBuyerRequest


class UserMapper:
    @staticmethod
    def buyer_mapper(request:RegisterBuyerRequest):
        return Buyer(name=request.name,email=request.email,password=request.password)

    @staticmethod
    def login_mapper(request:LoginBuyerRequest):
        return Buyer(email=request.email,password=request.password)




