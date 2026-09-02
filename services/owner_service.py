# from repositories.owner_repository import OwnerRepository
# from models.owner import Owner
#
# class OwnerService:
#     def __init__(self, repo:OwnerRepository):
#         self.repo = repo
#
#     def add_property(self, owner_id, data):
#         owner = Owner(**data, owner_id=owner_id)
#         return self.repo.save(owner)
#
#     def remove_property(self, property_id):
#         owner = self.repo.find_by_id(property_id)
#         if owner:
#             self.repo.delete(owner)
#
#     def update_property(self, property_id, data):
#         owner = self.repo.find_by_id(property_id)
#         if owner:
#             for key, value in data.items():
#                 setattr(owner, key, value)
#             return self.repo.save(owner)
#         return None
#
#     def view_properties(self, owner_id):
#         return self.repo.find_by_owner(owner_id)