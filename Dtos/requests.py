from pydantic import BaseModel

class RegisterBuyerRequest(BaseModel):
    name:str
    email:str
    password:str



class RegisterOwnerRequest(BaseModel):
    name:str
    email:str
    password:str


class LoginBuyerRequest(BaseModel):
    email:str
    password:str


class BuyPropertyRequest(BaseModel):
    price:int
    name:str
