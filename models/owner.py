from sqlalchemy import Column,Integer,ForeignKey,String
from sqlalchemy.orm import declarative_base, relationship
from database import Base


from models.user import User


class Owner(User):
    __tablename__ = 'owners'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    properties=relationship("Property", back_populates="owner")

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    location = Column(String, nullable=False)
    description = Column(String, nullable=True)

    owner_id = Column(Integer, ForeignKey("owners.owner_id"), nullable=False)
    owner = relationship("Owner", back_populates="properties")