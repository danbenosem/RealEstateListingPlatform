from models.user import User
from models.property import Property

class Buyer(User):
    saved_properties:list[Property]
