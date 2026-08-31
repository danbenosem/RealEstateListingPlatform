from pydantic import BaseModel


class RegisterResponse(BaseModel):
    success:bool
    message:str


class LoginResponse(BaseModel):
    success:bool
    message:str
    buyer_id:int | None=None


class BuyPropertyResponse(BaseModel):
    success: bool
    message: str


