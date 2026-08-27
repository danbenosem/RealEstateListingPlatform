from models.buyer import Buyer
from  repositories.buyer_repository import BuyerRepository


class InMemoryBuyerRepository(BuyerRepository):

    def __init__(self, session):
        self.session = session

    def find_by_id(self, buyer_id: int) -> Buyer:
        return self.session.query(Buyer).filter(Buyer.id == buyer_id).first()


    def find_all(self) -> dict[int, Buyer]:
        pass

    def delete_by_id(self, buyer_id: int) -> None:
        pass


    def update(self, buyer_id: int, data: dict) -> None:
        buyer= self.find_by_id(buyer_id)
        buyer.name= data["name"]
        buyer.email= data["email"]

        self.session.add(buyer)











    def save(self, buyer: Buyer) -> None:
        self.session.add(buyer)
        self.session.commit()




