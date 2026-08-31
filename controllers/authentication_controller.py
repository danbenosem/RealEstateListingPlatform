from fastapi import APIRouter,Depends

from Dtos.requests import RegisterBuyerRequest,LoginBuyerRequest
from services.authenticaton_service import AuthenticationService
from dependencies import get_authentication_service




router = APIRouter()

@router.post("/register")
def register_buyer(request:RegisterBuyerRequest,authentication_service:AuthenticationService=Depends(get_authentication_service)):
    return authentication_service.register_buyer(request)


@router.post("/login")
def login_buyer(request:LoginBuyerRequest,  authentication_service: AuthenticationService = Depends(get_authentication_service)):
    return  authentication_service.login_buyer(request)