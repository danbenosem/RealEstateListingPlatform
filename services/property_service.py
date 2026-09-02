from Dtos.responses import AddPropertyResponse, RemovePropertyInformationResponse, UpdatePropertyInformationResponse
from repositories.property_repository import PropertyRepository
from models.property import Property


class PropertyService:
    def __init__(self, repo: PropertyRepository):
        self.repo = repo

    def add_property(self, owner_id, data):
        property = Property(**data, owner_id=owner_id)
        self.repo.save(property)
        return AddPropertyResponse(
            success=True,
            message="Property successfully added",
            id= property.id
        )

    def remove_property(self, property_id):
        property = self.repo.find_by_id(property_id)
        if property is None:
            return RemovePropertyInformationResponse(
                success=False,
                message="Property not found"
            )

        self.repo.delete(property)
        return RemovePropertyInformationResponse(
            success=True,
            message="Property successfully removed"
        )

    def update_property(self, property_id, data):
        property = self.repo.find_by_id(property_id)
        if property is None:
            return UpdatePropertyInformationResponse(
                success=False,
                message="Property not found"
            )

        for key, value in data.items():
            setattr(property, key, value)
        self.repo.save(property)

        return UpdatePropertyInformationResponse(
            success=True,
            message="Property successfully updated",
            property_id= property.id
        )

    def view_properties(self, owner_id):
        return self.repo.find_by_owner(owner_id)


