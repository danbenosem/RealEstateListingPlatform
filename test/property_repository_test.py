import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models.property import Property
from models.owner import Owner
from repositories.property_repository import PropertyRepository


class PropertyRepositoryTest(unittest.TestCase):

    def setUp(self):

        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.repo = PropertyRepository(self.session)


        self.owner = Owner(name="Test Owner", email="owner@test.com", password="1234")
        self.session.add(self.owner)
        self.session.commit()

    def tearDown(self):
        self.session.close()

    def test_save_creates_property(self):
        property = Property(
            name="2 Bedroom Flat",
            price=50000,
            location="Lekki",
            description="Nice quiet flat",
            owner_id=self.owner.id
        )
        saved = self.repo.save(property)

        self.assertIsNotNone(saved.id)
        self.assertEqual(saved.name, "2 Bedroom Flat")

    def test_find_by_id_returns_correct_property(self):
        property = Property(
            name="Studio Apartment",
            price=20000,
            location="Yaba",
            description="Compact studio",
            owner_id=self.owner.id
        )
        saved = self.repo.save(property)

        found = self.repo.find_by_id(saved.id)

        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Studio Apartment")

    def test_find_by_id_returns_none_when_not_found(self):
        found = self.repo.find_by_id(999)
        self.assertIsNone(found)

    def test_find_by_owner_returns_all_properties_for_owner(self):
        self.repo.save(Property(
            name="Seunfunmi", price=100000, location="Ikeja",
            description="First house", owner_id=self.owner.id
        ))
        self.repo.save(Property(
            name="funmi", price=150000, location="Ikeja",
            description="Second house", owner_id=self.owner.id
        ))

        results = self.repo.find_by_owner(self.owner.id)

        self.assertEqual(len(results), 2)

    def test_delete_removes_property(self):
        property = Property(
            name="Old Listing", price=30000, location="Surulere",
            description="To be deleted", owner_id=self.owner.id
        )
        saved = self.repo.save(property)
        property_id = saved.id

        self.repo.delete(saved)

        self.assertIsNone(self.repo.find_by_id(property_id))


