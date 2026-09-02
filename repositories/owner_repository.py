
from models.owner import Owner
from sqlalchemy.exc import IntegrityError



class OwnerRepository:

    def __init__(self, session):
        self.session = session

    def save(self, owner: Owner) -> None:
        try:
            self.session.add(owner)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

    def find_by_id(self, owner_id: int) -> Owner:
        return self.session.query(Owner).filter(
            Owner.id == owner_id
        ).first()

    def find_all(self) -> dict[int, Owner]:
        owners = self.session.query(Owner).all()
        dict_owner = {owner.id: owner for owner in owners}
        return dict_owner

    def delete_by_id(self, owner_id: int) -> None:
        owner = self.find_by_id(owner_id)

        if owner is not None:
            self.session.delete(owner)
            self.session.commit()

    def update(self, owner_id: int, data: dict) -> None:
        owner = self.find_by_id(owner_id)

        owner.name = data["name"]
        owner.email = data["email"]

        self.session.add(owner)
        self.session.commit()

    def find_by_email(self, owner_email: str):
        return self.session.query(Owner).filter(
            Owner.email == owner_email
        ).first()

    def create_from_user_id(self, user_id: int) -> None:
        try:
            self.session.execute(
                Owner.__table__.insert().values(id=user_id)
            )
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise