from unittest import TestCase
from repositories.property_repository import PropertyRepository
from database import SessionLocal,Base,engine
from services.buyer_service import BuyerService
from models.property import Property
from models.owner import Owner
from models.buyer import Buyer
from Dtos.requests import RegisterUserRequest, BuyPropertyRequest
from services.authentication_service import AuthenticationService
from repositories.in_memory_buyer_repository import InMemoryBuyerRepository


class BuyerServiceTest(TestCase):

    def setUp(self):

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

        self.session = SessionLocal()
        self.property_repo= PropertyRepository(self.session)
        self.buyer_repo=InMemoryBuyerRepository(self.session)
        self.buyer_service=BuyerService(self.property_repo,self.buyer_repo)
        self.buyer_repo= InMemoryBuyerRepository(self.session)
        self.authentication_service= AuthenticationService(self.buyer_repo)

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(bind=engine)


    def test_that_buyer_can_find_property_by_price(self):
        property = Property(name="2 bedroom flat",  price=500,description="Nice apartment", location="Lagos" )

        self.property_repo.save(property)
        result= self.buyer_service.find_property_by_price(500)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].price, 500)


    def test_that_find_property_by_location(self):
        property= Property(name="2 bedroom flat",  price=500,description="Nice apartment", location="Lagos")

        self.property_repo.save(property)
        result= self.buyer_service.find_property_by_location("lagos")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].location, "Lagos")

    def test_that_buyer_can_buy_property(self):
        property= Property(name="2 bedroom flat",  price=500,description="Nice apartment", location="Lagos")
        buyer= Buyer(name="dan",email="dan@gmail.com",password="1234")

        self.property_repo.save(property)
        self.buyer_repo.save(buyer)
        price=500

        buy_request=BuyPropertyRequest(name="2 bedroom flat",price=500)

        response=self.buyer_service.buy_property(buyer.id,buy_request)
        self.assertTrue(response.success)

