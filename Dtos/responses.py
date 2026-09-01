from pydantic import BaseModel


class RegisterResponse(BaseModel):
    success:bool
    message:str


class LoginUserResponse(BaseModel):
    success:bool
    message:str
    user_id:int | None=None


class LogoutUserResponse(BaseModel):
    success:bool
    message:str

class BuyPropertyResponse(BaseModel):
    success: bool
    message: str


class SellPropertyResponse(BaseModel):
    success: bool
    message: str


class AddPropertyResponse(BaseModel):
     success: bool
     message: str


class UpdatePropertyInformationResponse(BaseModel):
    success: bool
    message: str


class RemovePropertyInformationResponse(BaseModel):
    success: bool
    message: str

