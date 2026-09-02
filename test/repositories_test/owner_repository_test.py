
from unittest import TestCase

from database import SessionLocal, Base, engine
from models.owner import Owner
from models.property import Property
from models.buyer import Buyer
from repositories.owner_repository import OwnerRepository


class TestOwnerRepository(TestCase):

    def setUp(self):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        self.session = SessionLocal()
        self.repository = OwnerRepository(self.session)

    def tearDown(self):
        self.session.close()

    def test_that_owner_can_be_saved(self):
        owner = Owner(
            name="dan",
            email="dan@gmail.com",
            password="123"
        )

        self.repository.save(owner)

        self.assertIsNotNone(owner.id)

    def test_that_owner_can_be_found_by_id(self):
        owner = Owner(
            name="dan",
            email="dan@gmail.com",
            password="123"
        )

        self.repository.save(owner)

        found_owner = self.repository.find_by_id(owner.id)

        self.assertIsNotNone(found_owner)
        self.assertEqual(found_owner.name, "dan")
        self.assertEqual(found_owner.email, "dan@gmail.com")

    def test_that_all_owners_can_be_found(self):
        owner1 = Owner(
            name="dan",
            email="dan@gmail.com",
            password="123"
        )

        owner2 = Owner(
            name="john",
            email="john@gmail.com",
            password="456"
        )

        self.repository.save(owner1)
        self.repository.save(owner2)

        owners = self.repository.find_all()

        self.assertEqual(len(owners), 2)
        self.assertIn(owner1.id, owners)
        self.assertIn(owner2.id, owners)

    def test_that_owner_can_be_found_by_email(self):
        owner = Owner(
            name="dan",
            email="dan@gmail.com",
            password="123"
        )

        self.repository.save(owner)

        found_owner = self.repository.find_by_email(
            "dan@gmail.com"
        )

        self.assertIsNotNone(found_owner)
        self.assertEqual(found_owner.email, "dan@gmail.com")

    def test_that_non_existing_owner_returns_none(self):
        owner = self.repository.find_by_email(
            "doesnotexist@gmail.com"
        )

        self.assertIsNone(owner)

    def test_that_owner_can_be_deleted(self):
        owner = Owner(
            name="dan",
            email="dan@gmail.com",
            password="123"
        )

        self.repository.save(owner)

        owner_id = owner.id

        self.repository.delete_by_id(owner_id)

        found_owner = self.repository.find_by_id(owner_id)

        self.assertIsNone(found_owner)

    def test_that_owner_can_be_updated(self):
        owner = Owner(
            name="dan",
            email="dan@gmail.com",
            password="123"
        )

        self.repository.save(owner)

        self.repository.update(
            owner.id,
            {
                "name": "daniel",
                "email": "daniel@gmail.com"
            }
        )

        updated_owner = self.repository.find_by_id(owner.id)

        self.assertEqual(updated_owner.name, "daniel")
        self.assertEqual(updated_owner.email, "daniel@gmail.com")

