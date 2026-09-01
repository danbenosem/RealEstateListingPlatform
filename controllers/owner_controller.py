from fastapi import APIRouter
from sqlalchemy.orm import Session
from services.property_service import PropertyService
from dependencies import property_services

router = APIRouter()

