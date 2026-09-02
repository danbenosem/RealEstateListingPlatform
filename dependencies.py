from database import SessionLocal
from repositories.property_repository import PropertyRepository
from services.buyer_service import BuyerService
from repositories.in_memory_buyer_repository import InMemoryBuyerRepository
from repositories.user_repository import UserRepository
from services.authentication_service import AuthenticationService
from services.property_service import PropertyService


def get_buyer_service():
    session = SessionLocal()
    property_repo = PropertyRepository(session)
    buyer_repo=InMemoryBuyerRepository(session)
    return BuyerService(property_repo,buyer_repo)


def get_authentication_service():
    session = SessionLocal()
    user_repo= UserRepository(session)
    return AuthenticationService(user_repo)

def get_property_service():
    session = SessionLocal()
    property_repo = PropertyRepository(session)

    return PropertyService(property_repo)



from repositories.owner_repository import OwnerRepository
from services.owner_service import OwnerService


def get_owner_service():
    session = SessionLocal()
    owner_repo = OwnerRepository(session)

    return OwnerService(owner_repo) 
