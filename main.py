from fastapi import FastAPI

from database import Base, engine
from models.user import User
from models.owner import Owner
from models.buyer import Buyer
from models.property import Property

Base.metadata.create_all(bind=engine)

app = FastAPI()