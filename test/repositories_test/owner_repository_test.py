from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from models.user import User
from models.property import Property
from models.owner import Owner
from models.buyer import Buyer
from repositories.owner_repository import OwnerRepository
from repositories.user_repository import UserRepository


class OwnerRepositoryTest(TestCase):

    def setUp(self):

        self.engine = create_engine("sqlite:///:memory:")

        Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)

        self.session = Session()

        self.repository = OwnerRepository(self.session)

    def tearDown(self):

        self.session.close()

        Base.metadata.drop_all(self.engine)

    def test_that_existing_user_can_become_owner(self):

        user = User(
            name="daniel",
            email="owner@gmail.com",
            password="1234"
        )

        user_repository = UserRepository(self.session)

        user_repository.save(user)

        self.repository.create_from_user_id(user.id)

        saved_owner = self.repository.find_by_id(user.id)


        self.assertEqual(saved_owner.id, user.id)