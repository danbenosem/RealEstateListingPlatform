from models.user import User
from models.property import Property

class Owner(User):
    properties:list[Property]