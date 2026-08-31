
from typing import List, Optional

from sqlalchemy.orm import Session

from app import models, schemas


class OwnerRepository:
    def __init__(self, db: Session):
        self.db = db

    # ---------- Owner ----------

    def create(self, owner_in: schemas.OwnerCreate) -> models.Owner:
        owner = models.Owner(
            name=owner_in.name,
            email=owner_in.email,
            password=owner_in.password,  # hashed by the service layer
            is_logged_in=False,
        )
        self.db.add(owner)
        self.db.commit()
        self.db.refresh(owner)
        return owner

    def get_by_id(self, owner_id: int) -> Optional[models.Owner]:
        return (
            self.db.query(models.Owner)
            .filter(models.Owner.owner_id == owner_id)
            .first()
        )

    def get_by_email(self, email: str) -> Optional[models.Owner]:
        return (
            self.db.query(models.Owner)
            .filter(models.Owner.email == email)
            .first()
        )

    def get_all(self, skip: int = 0, limit: int = 100) -> List[models.Owner]:
        return self.db.query(models.Owner).offset(skip).limit(limit).all()

    def delete(self, owner: models.Owner) -> None:
        self.db.delete(owner)
        self.db.commit()

    # ---------- Property (AddProperty / removeProperty / updateProperty / viewProperties) ----------

    def add_property(
        self, owner_id: int, property_in: schemas.PropertyCreate
    ) -> models.Property:
        prop = models.Property(**property_in.model_dump(), owner_id=owner_id)
        self.db.add(prop)
        self.db.commit()
        self.db.refresh(prop)
        return prop

    def get_property(self, owner_id: int, property_id: int) -> Optional[models.Property]:
        return (
            self.db.query(models.Property)
            .filter(
                models.Property.id == property_id,
                models.Property.owner_id == owner_id,
            )
            .first()
        )

    def view_properties(self, owner_id: int) -> List[models.Property]:
        return (
            self.db.query(models.Property)
            .filter(models.Property.owner_id == owner_id)
            .all()
        )

    def update_property(
        self, prop: models.Property, property_in: schemas.PropertyUpdate
    ) -> models.Property:
        for field, value in property_in.model_dump(exclude_unset=True).items():
            setattr(prop, field, value)
        self.db.commit()
        self.db.refresh(prop)
        return prop

    def remove_property(self, prop: models.Property) -> None:
        self.db.delete(prop)
        self.db.commit()