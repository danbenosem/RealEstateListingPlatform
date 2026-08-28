from repositories.property_repository import PropertyRepository
from models.property import Property


class PropertyService:
    def __init__(self, repo: PropertyRepository):
        self.repo = repo

    def add_property(self, owner_id, data):
        property = Property(**data, owner_id=owner_id)
        return self.repo.save(property)

    def remove_property(self, property_id):
        property = self.repo.find_by_id(property_id)
        if property:
            self.repo.delete(property)

    def update_property(self, property_id, data):
        property = self.repo.find_by_id(property_id)
        if property:
            for key, value in data.items():
                setattr(property, key, value)
            return self.repo.save(property)
        return None

    def view_properties(self, owner_id):
        return self.repo.find_by_owner(owner_id)