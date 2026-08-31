from sqlalchemy import Column,Integer,ForeignKey
from sqlalchemy.orm import declarative_base, relationship


from models.user import User


class Owner(User):
    __tablename__ = 'owners'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    properties=relationship("Property", back_populates="owner")

