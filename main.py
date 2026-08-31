from fastapi import FastAPI
from database import Base,engine
from models.user import User
from models.buyer import Buyer
from models.owner import Owner
from models.property import Property
Base.metadata.create_all(engine)





from controllers.authentication_controller import router as authentication_router
from controllers.buyer_controller import router as buyer_router


app=FastAPI()

app.include_router(authentication_router)
app.include_router(buyer_router)