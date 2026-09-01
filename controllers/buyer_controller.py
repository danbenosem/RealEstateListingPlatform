from fastapi import APIRouter, Depends
from Dtos.requests import BuyPropertyRequest
from services.buyer_service import BuyerService
from dependencies import get_buyer_service

router = APIRouter()

@router.get("buyer/properties/price/{price}")
def find_property_by_price(
    price: int,buyer_service: BuyerService = Depends(get_buyer_service)):
    return buyer_service.find_property_by_price(price)


@router.get("buyer/properties/location/{location}")
def find_property_by_location(location: str, buyer_service: BuyerService = Depends(get_buyer_service)):
    return buyer_service.find_property_by_location(location)


@router.post("buyer/buy")
def buy_property(buyer_id:int,request:BuyPropertyRequest,buyer_service:BuyerService=Depends(get_buyer_service)):
    return buyer_service.buy_property(buyer_id,request)