from unittest import TestCase

from Dtos.responses import LoginResponse
from database import SessionLocal,Base,engine

from services.authenticaton_service import AuthenticationService
from Dtos.requests import RegisterBuyerRequest, LoginBuyerRequest

from repositories.in_memory_buyer_repository import InMemoryBuyerRepository
from models.user import User
from models.buyer import Buyer
from models.owner import Owner
from models.property import Property

class TestAuthenticationService(TestCase):

    def setUp(self):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        self.session = SessionLocal()

        self.repository = InMemoryBuyerRepository(self.session)
        self.authenticaton_service = AuthenticationService(self.repository)

    def tearDown(self):
        self.session.close()

    def test_that_user_can_register_as_buyer(self):


        buyer = RegisterBuyerRequest(name="dan",email="dan456@gmail.com",password="1234")


        response= self.authenticaton_service.register_buyer(buyer)

        self.assertTrue(response.success)

    def test_that_registered_user_cannot_register(self):
        buyerRequest= RegisterBuyerRequest(name="dan",email="dan123@gmail.com", password="123")
        self.authenticaton_service.register_buyer(buyerRequest)
        response= self.authenticaton_service.register_buyer(buyerRequest)
        self.assertFalse(response.success)


    def test_that_registered_user_can_login(self):
        buyerRequest=  RegisterBuyerRequest(name="dan",email="dan123@gmail.com", password="123")
        self.authenticaton_service.register_buyer(buyerRequest)
        login_request=LoginBuyerRequest(email="dan123@gmail.com",password="123")
        response=self.authenticaton_service.login_buyer(login_request)

        self.assertTrue(response.success)

    def test_that_unregistred_user_cannot_login(self):
        buyerRequest=  RegisterBuyerRequest(name="dan",email="dan123@gmail.com", password="123")
        self.authenticaton_service.register_buyer(buyerRequest)
        login_request=LoginBuyerRequest(email="dan12w3@gmail.com",password="1w23")
        response=self.authenticaton_service.login_buyer(login_request)

        self.assertFalse(response.success)




























