from unittest import TestCase

from database import SessionLocal,Base,engine

from services.authentication_service import AuthenticationService
from Dtos.requests import RegisterUserRequest, LoginUserRequest

from repositories.in_memory_buyer_repository import InMemoryBuyerRepository

class TestAuthenticationService(TestCase):

    def setUp(self):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        self.session = SessionLocal()

        self.repository = InMemoryBuyerRepository(self.session)
        self.authentication_service = AuthenticationService(self.repository)

    def tearDown(self):
        self.session.close()

    def test_that_user_can_register_as_buyer(self):


        buyer = RegisterUserRequest(name="dan",email="dan456@gmail.com",password="1234")


        response= self.authentication_service.register_user(buyer)


        self.assertTrue(response.success)

    def test_that_registered_user_cannot_register(self):
        user_request= RegisterUserRequest(name="dan",email="dan123@gmail.com", password="123")
        self.authentication_service.register_user(user_request)
        response= self.authentication_service.register_user(user_request)
        self.assertFalse(response.success)


    def test_that_registered_user_can_login(self):
        user_request=  RegisterUserRequest(name="dan",email="dan123@gmail.com", password="123")
        self.authentication_service.register_user(user_request)
        login_request=LoginUserRequest(email="dan123@gmail.com",password="123")
        response=self.authentication_service.login_user(login_request)

        self.assertTrue(response.success)

    def test_that_unregistered_user_cannot_login(self):
        user_request=  RegisterUserRequest(name="dan",email="dan123@gmail.com", password="123")
        self.authentication_service.register_user(user_request)
        login_request=LoginUserRequest(email="dan12w3@gmail.com",password="1w23")
        response=self.authentication_service.login_user(login_request)

        self.assertFalse(response.success)




























