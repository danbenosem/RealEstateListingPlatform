from database import SessionLocal
from models.property import Property
from models.owner import Owner
from models.buyer import Buyer

session = SessionLocal()

property = Property(
    name="2 bedroom flat",
    price=500,
    description="Nice apartment",
    location="Lagos"
)

session.add(property)
session.commit()
session.close()