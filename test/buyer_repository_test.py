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
    # def setUpClass(cls):
    #     cls.engine= create_engine('sqlite:///:memory:')
    #
    #     Base.metadata.create_all(cls.engine)
    #
    #     cls.Session= sessionmaker(bind=cls.engine)

    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session= Session()
        self.repository = InMemoryBuyerRepository(self.session)

    def tearDown(self):
        # self.session.rollback()
        self.session.close()

        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
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


    def test_that_buyer_can_be_deleted(self):
        buyer = Buyer(name="daniel", email="gggghre@gmail.com", password="1234")
        self.repository.save(buyer)
        self.repository.delete_by_id(buyer.id)
        buyer=self.repository.find_by_id(buyer.id)
        self.assertIsNone(buyer)


    def test_that_all_buyers_can_be_found(self):
        buyer = Buyer(name="daniel", email="gggghre@gmail.com", password="1234")
        buyer2= Buyer(name="isreal", email="ggg@gmail.com", password="1234")
        buyer3 = Buyer(name="obi", email="gghre@gmail.com", password="1234")

        self.repository.save(buyer)
        self.repository.save(buyer2)
        self.repository.save(buyer3)

        saved_users= self.repository.find_all()

        self.assertIsInstance(saved_users,dict)

















