
from unittest import TestCase

from database import SessionLocal, Base, engine
from models.user import User
from repositories.user_repository import UserRepository


class TestUserRepository(TestCase):

    def setUp(self):
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

        self.session = SessionLocal()
        self.repository = UserRepository(self.session)

    def tearDown(self):
        self.session.close()

    def test_that_user_can_be_saved(self):
        user = User(
            name="dan",
            email="dan123@gmail.com",
            password="123"
        )

        self.repository.save(user)

        self.assertIsNotNone(user.id)

    def test_that_user_can_be_found_by_id(self):
        user = User(
            name="dan",
            email="dan123@gmail.com",
            password="123"
        )

        self.repository.save(user)

        found_user = self.repository.find_by_id(user.id)

        self.assertEqual(found_user.name, "dan")
        self.assertEqual(found_user.email, "dan123@gmail.com")

    def test_that_user_can_be_found_by_email(self):
        user = User(
            name="dan",
            email="dan123@gmail.com",
            password="123"
        )

        self.repository.save(user)

        found_user = self.repository.find_by_email("dan123@gmail.com")


        self.assertEqual(found_user.name, "dan")
        self.assertEqual(found_user.email, "dan123@gmail.com")

    def test_that_non_existing_user_returns_none(self):
        found_user = self.repository.find_by_email("doesnotexist@gmail.com")

        self.assertIsNone(found_user)

    def test_that_user_can_be_found_by_id_after_saving(self):
        user = User(
            name="john",
            email="john123@gmail.com",
            password="456"
        )

        self.repository.save(user)

        found_user = self.repository.find_by_id(user.id)

        self.assertEqual(found_user.id, user.id)
