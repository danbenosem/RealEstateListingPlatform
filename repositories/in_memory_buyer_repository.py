from models.buyer import Buyer
from  repositories.buyer_repository import BuyerRepository
from sqlalchemy.exc import IntegrityError


class InMemoryBuyerRepository(BuyerRepository):

    def __init__(self, session):
        self.session = session

    def save(self, buyer: Buyer) -> None:
        try:
            self.session.add(buyer)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

    def find_by_id(self, buyer_id: int) -> Buyer:
        return self.session.query(Buyer).filter(Buyer.id == buyer_id).first()


    def find_all(self) -> dict[int, Buyer]:
        buyers=self.session.query(Buyer).all()
        dict_buyer= {buyer.id: buyer for buyer in buyers}
        return dict_buyer

    def delete_by_id(self, buyer_id: int) -> None:
        buyer= self.find_by_id(buyer_id)
        self.session.delete(buyer)
        self.session.commit()



    def update(self, buyer_id: int, data: dict) -> None:
        buyer= self.find_by_id(buyer_id)
        buyer.name= data["name"]
        buyer.email= data["email"]

        self.session.add(buyer)

    def find_by_email(self,buyer_email:str):
        return self.session.query(Buyer).filter(Buyer.email==buyer_email).first()


