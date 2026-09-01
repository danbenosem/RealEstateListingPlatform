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
