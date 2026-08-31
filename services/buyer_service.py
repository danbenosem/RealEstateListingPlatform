from Dtos.requests import BuyPropertyRequest
from Dtos.responses import BuyPropertyResponse
from models.property import Property


class BuyerService:
    def __init__(self,propertyRepo,buyerRepo):
        self.propertyRepo= propertyRepo
        self.buyerRepo= buyerRepo


    def find_property_by_price(self,price):
        return self.propertyRepo.find_property_by_price(price)


    def find_property_by_location(self,location):
        return self.propertyRepo.find_by_location(location)

    def buy_property(self, buyer_id, request:BuyPropertyRequest):

        property= self.propertyRepo.find_by_name(request.name)
        if property is None:
            return BuyPropertyResponse(
                success=False,
                message="Property not found"
            )

        if request.price != property.price:
            return BuyPropertyResponse(
                success=False,
                message="incorrect price"
            )
        buyer=self.buyerRepo.find_by_id(buyer_id)
        property.buyer=buyer
        self.propertyRepo.save(property)

        return BuyPropertyResponse(
            success=True,
            message="Property purchased successfully"
        )






