
from typing import List

from sqlalchemy.orm import Session

from models.owner import Owner
from models.property import PropertyCreate,Property




class OwnerRepository:
    def __init__(self, db: Session):
        self.db = db





    def get_by_id(self, owner_id: int) :
        return (
            self.db.query(Owner)
            .filter(Owner.owner_id == owner_id)
            .first()
        )

    def get_by_email(self, email: str) :
        return (
            self.db.query(Owner)
            .filter(Owner.email == email)
            .first()
        )

    def get_all(self):
        return self.db.query(Owner).all()

    def delete(self, owner: Owner) -> None:
        self.db.delete(owner)
        self.db.commit()



    def add_property(
        self, owner_id: int, property_in: PropertyCreate
    ) :
        prop = Property(**property_in.model_dump(), owner_id=owner_id)
        self.db.add(prop)
        self.db.commit()
        self.db.refresh(prop)
        return prop

    def get_property(self, owner_id: int, property_id: int) :
        return (
            self.db.query(Property)
            .filter(
                Property.id == property_id,
                Property.owner_id == owner_id,
            )
            .first()
        )

    def view_properties(self, owner_id: int):
        return (
            self.db.query(Property)
            .filter(Property.owner_id == owner_id)
            .all()
        )

    def update_property(
        self, prop: Property, property_in: PropertyCreate
    ) -> Property:
        for field, value in property_in.model_dump(exclude_unset=True).items():
            setattr(prop, field, value)
        self.db.commit()
        self.db.refresh(prop)
        return prop

    def remove_property(self, prop: Property) -> None:
        self.db.delete(prop)
        self.db.commit()