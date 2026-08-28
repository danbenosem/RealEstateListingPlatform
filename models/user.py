from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel, Field
from database import Base



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)



class UserCreate(BaseModel):
    name:str
    email:str
    password:str
    isLoggedIn:bool

