from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import UUID

from models.buyer import Buyer



class BuyerRepository(ABC):



    @abstractmethod
    def save(self,buyer:Buyer)->None:
        ...

    @abstractmethod
    def update(self,buyer_id:int,data:dict)->None:
        ...

    @abstractmethod
    def find_by_id(self,buyer_id:int)->Buyer:
        ...

    @abstractmethod
    def find_all(self)->dict[int,Buyer]:
        ...

    @abstractmethod
    def delete_by_id(self,buyer_id:int)->None:
           ...


