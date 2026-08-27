from models.user import User
from models.property import Property

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

class Buyer(User):
    __tablename__ = "buyers"

    id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    properties = relationship("Property", back_populates="buyer")
