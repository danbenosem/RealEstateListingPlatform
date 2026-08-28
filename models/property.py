from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey("owners.id"), nullable=False)
    owner = relationship("Owner", back_populates="properties")

    buyer_id = Column(Integer, ForeignKey("buyers.id"), nullable=True)
    buyer = relationship("Buyer", back_populates="properties")


class PropertyCreate(BaseModel):
    name: str
    price: int
    location: str
    description: str