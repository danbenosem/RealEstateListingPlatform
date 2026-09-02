import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models.property import Property
from models.owner import Owner
from models.buyer import Buyer
from repositories.property_repository import PropertyRepository
from services.property_service import PropertyService


class PropertyServiceTest(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.repo = PropertyRepository(self.session)
        self.service = PropertyService(self.repo)

        self.owner = Owner(name="Test Owner", email="owner@test.com", password="1234")
        self.session.add(self.owner)
        self.session.commit()

    def tearDown(self):
        self.session.close()

    def test_add_property(self):
        data = {
            "name": "2 Bedroom Flat",
            "price": 50000,
            "location": "Lekki",
            "description": "Nice quiet flat"
        }

        result = self.service.add_property(owner_id=self.owner.id, data=data)

        self.assertIsNotNone(result.id)
        self.assertEqual(result.name, "2 Bedroom Flat")

    def test_remove_property(self):
        data = {
            "name": "Old Listing",
            "price": 30000,
            "location": "Surulere",
            "description": "To be deleted"
        }
        added = self.service.add_property(owner_id=self.owner.id, data=data)
        property_id = added.id

        self.service.remove_property(property_id)

        self.assertIsNone(self.repo.find_by_id(property_id))

    def test_update_property(self):
        data = {
            "name": "Studio Apartment",
            "price": 20000,
            "location": "Yaba",
            "description": "Compact studio"
        }
        added = self.service.add_property(owner_id=self.owner.id, data=data)

        self.service.update_property(added.id, {"price": 25000})

        updated = self.repo.find_by_id(added.id)
        self.assertEqual(updated.price, 25000)

    def test_view_properties(self):
        self.service.add_property(owner_id=self.owner.id, data={
            "name": "House A", "price": 100000,
            "location": "Ikeja", "description": "First house"
        })
        self.service.add_property(owner_id=self.owner.id, data={
            "name": "House B", "price": 150000,
            "location": "Ikeja", "description": "Second house"
        })

        results = self.service.view_properties(self.owner.id)

        self.assertEqual(len(results), 2)


