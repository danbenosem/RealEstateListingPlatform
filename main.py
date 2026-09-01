from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from database import Base,engine
from models.user import User
from models.buyer import Buyer
from models.owner import Owner
from models.property import Property
Base.metadata.create_all(engine)






from controllers.authentication_controller import router as authentication_router
from controllers.buyer_controller import router as buyer_router


app=FastAPI()

origins = [



    "http://localhost:5500",
    "http://127.0.0.1:5500",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(authentication_router)
app.include_router(buyer_router)