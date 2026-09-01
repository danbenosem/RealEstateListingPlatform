from fastapi import APIRouter,Depends

from Dtos.requests import RegisterUserRequest,LoginUserRequest,LogOutUserRequest
from services.authentication_service import AuthenticationService
from dependencies import get_authentication_service




router = APIRouter()

@router.post("/register")
def register_user(request:RegisterUserRequest,authentication_service:AuthenticationService=Depends(get_authentication_service)):
    return authentication_service.register_user(request)


@router.post("/login")
def login_user(request:LoginUserRequest,  authentication_service: AuthenticationService = Depends(get_authentication_service)):
    return  authentication_service.login_user(request)


@router.post("/logout")
def logout_user(request:LogOutUserRequest, authentication_service: AuthenticationService = Depends(get_authentication_service)):
    return authentication_service.logout_user(request)