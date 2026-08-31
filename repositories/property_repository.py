from sqlalchemy.orm import Session
from models.property import Property


class PropertyRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, property: Property) -> Property:
        self.db.add(property)
        self.db.commit()
        self.db.refresh(property)
        return property

    def find_by_id(self, property_id: int) -> Property | None:
        return self.db.query(Property).filter(Property.id == property_id).first()

    def find_by_owner(self, owner_id: int) -> list[Property]:
        return self.db.query(Property).filter(Property.owner_id == owner_id).all()

    def find_property_by_price(self, price: int) -> list[Property]:
        return self.db.query(Property).filter(Property.price == price).all()

    def find_by_location(self, location: str) -> list[Property]:
        return self.db.query(Property).filter(Property.location.ilike(location)).all()

    def find_by_name(self,name:str) ->property | None:
        return self.db.query(Property).filter(Property.name == name).first()

    def delete(self, property: Property) -> None:
        self.db.delete(property)
        self.db.commit()