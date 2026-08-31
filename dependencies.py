from database import SessionLocal
from repositories.property_repository import PropertyRepository
from services.buyer_service import BuyerService
from repositories.in_memory_buyer_repository import InMemoryBuyerRepository
from services.authenticaton_service import AuthenticationService


def get_buyer_service():
    session = SessionLocal()
    property_repo = PropertyRepository(session)
    buyer_repo=InMemoryBuyerRepository(session)
    return BuyerService(property_repo,buyer_repo)


def get_authentication_service():
    session = SessionLocal()
    buyer_repo = InMemoryBuyerRepository(session)
    return AuthenticationService(buyer_repo)