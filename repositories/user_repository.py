from models.user import User
from sqlalchemy.exc import IntegrityError


class UserRepository:

    def __init__(self, session):
        self.session = session

    def save(self, user: User) -> None:
        try:
            self.session.add(user)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

    def find_by_id(self, user_id: int):
        return self.session.query(User).filter(User.id == user_id).first()

    def find_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()