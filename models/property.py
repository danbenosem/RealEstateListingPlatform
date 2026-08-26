from pydantic import BaseModel



class Property(BaseModel):
    name: str
    price: int
    location: str
    description: str


    