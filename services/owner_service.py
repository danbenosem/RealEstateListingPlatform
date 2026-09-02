from sqlalchemy.exc import IntegrityError
from Dtos.responses import CreateOwnerResponse


class OwnerService:

    def __init__(self, ownerRepo):
        self.ownerRepo = ownerRepo

    def create_owner(self, user_id):

        existing_owner = self.ownerRepo.find_by_id(user_id)

        if existing_owner is not None:
            return CreateOwnerResponse(
                success=False,
                message="User is already an owner"
            )

        try:
            self.ownerRepo.create_from_user_id(user_id)

            return CreateOwnerResponse(
                success=True,
                message="Owner created successfully"
            )

        except IntegrityError:
            return CreateOwnerResponse(
                success=False,
                message="User does not exist"
            )