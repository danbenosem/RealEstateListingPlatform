from fastapi import APIRouter, Depends

from Dtos.requests import AddPropertyRequest, UpdatePropertyInformationRequest
from services.property_service import PropertyService
from dependencies import get_property_service
from services.owner_service import OwnerService
from dependencies import get_owner_service

router = APIRouter()

@router.post("/owners/{owner_id}/properties")
def add_property(owner_id: int, request: AddPropertyRequest, property_service: PropertyService = Depends(get_property_service)):
    return property_service.add_property(owner_id, request.model_dump())


@router.put("/owners/{owner_id}/properties/{property_id}")
def update_property(owner_id: int, property_id: int, request: UpdatePropertyInformationRequest, property_service: PropertyService = Depends(get_property_service)):
    return property_service.update_property(property_id, request.model_dump())


@router.delete("/owners/{owner_id}/properties/{property_id}")
def remove_property(owner_id: int, property_id: int, property_service: PropertyService = Depends(get_property_service)):
    return property_service.remove_property(property_id)



@router.post("/owners/{user_id}")
def create_owner(
    user_id: int,
    owner_service: OwnerService = Depends(get_owner_service)
):
    return owner_service.create_owner(user_id)