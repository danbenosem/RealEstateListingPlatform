from os import name
from unittest import TestCase
from models.buyer import Buyer
from models.owner import Owner
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models.property import Property
from repositories.in_memory_buyer_repository import InMemoryBuyerRepository

class BuyerRepositoryTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine= create_engine('sqlite:///:memory:')

        Base.metadata.create_all(cls.engine)

        cls.Session= sessionmaker(bind=cls.engine)

    def setUp(self):
        self.session= self.Session()
        self.repository = InMemoryBuyerRepository(self.session)

    def tearDown(self):
        self.session.close()


    def test_that_buyer_can_be_saved_repo(self):
        buyer=Buyer(name="daniel",email="gggghre@gmail.com",password="1234")
        self.repository.save(buyer)
        saved_buyer= self.session.query(Buyer).filter_by(email=buyer.email).first()
        self.assertEqual(saved_buyer.name,buyer.name)


    def test_that_buyer_can_be_be_found_byId(self):
        buyer = Buyer(name="daniel", email="gggghre@gmail.com", password="1234")
        self.repository.save(buyer)
        saved_buyer= self.repository.find_by_id(buyer.id)
        self.assertEqual(buyer.name,saved_buyer.name)


    def test_that_buyer_can_be_updated(self):
        buyer = Buyer(name="daniel", email="gggghre@gmail.com", password="1234")
        self.repository.save(buyer)
        self.repository.update(buyer.id,{"name":"danu",
                                                 "email":"dan@gmail.com"})

        updated_user= self.repository.find_by_id(buyer.id)
        self.assertNotEqual(updated_user.name,"daniel")














