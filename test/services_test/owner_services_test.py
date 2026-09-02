from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from models.user import User
from models.property import Property
from models.owner import Owner
from models.buyer import Buyer
from repositories.user_repository import UserRepository
from repositories.owner_repository import OwnerRepository
from services.owner_service import OwnerService


class OwnerServiceTest(TestCase):

    def setUp(self):

        self.engine = create_engine("sqlite:///:memory:")

        Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)

        self.session = Session()

        self.user_repository = UserRepository(self.session)
        self.owner_repository = OwnerRepository(self.session)

        self.service = OwnerService(self.owner_repository)

    def tearDown(self):

        self.session.close()

        Base.metadata.drop_all(self.engine)

    def test_that_existing_user_can_become_owner(self):

        user = User(
            name="daniel",
            email="owner@gmail.com",
            password="1234"
        )

        self.user_repository.save(user)

        response = self.service.create_owner(user.id)

        self.assertTrue(response.success)
        self.assertEqual(
            response.message,
            "Owner created successfully"
        )

        saved_owner = self.owner_repository.find_by_id(user.id)

        self.assertIsNotNone(saved_owner)
        self.assertEqual(saved_owner.id, user.id)

    def test_that_user_cannot_become_owner_twice(self):

        user = User(
            name="daniel",
            email="owner2@gmail.com",
            password="1234"
        )

        self.user_repository.save(user)

        self.service.create_owner(user.id)

        response = self.service.create_owner(user.id)

        self.assertFalse(response.success)
        self.assertEqual(
            response.message,
            "User is already an owner"
        )