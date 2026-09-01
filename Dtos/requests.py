from pydantic import BaseModel

class RegisterUserRequest(BaseModel):
    name:str
    email:str
    password:str



class LoginUserRequest(BaseModel):
    email:str
    password:str


class LogOutUserRequest(BaseModel):
    email:str


class BuyPropertyRequest(BaseModel):
    price:int
    name:str

class SellPropertyRequest(BaseModel):
    price:int
    description:str
    location:str


class AddPropertyRequest(BaseModel):
    name:str
    price:int
    description:str
    location:str


class UpdatePropertyInformationRequest(BaseModel):
    name:str
    price:int
    description:str
    location:str
