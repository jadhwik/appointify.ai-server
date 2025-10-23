from pydantic import EmailStr
from sqlmodel import SQLModel, Field, create_engine, Session, select

from app.common.models import AbstractTransactionalModel
from app.common.views import AbstractDetailedView


class Users(AbstractTransactionalModel):
    name: str = Field(..., min_length=3, max_length=255)
    email: EmailStr = Field(...)
    phone: str = Field(..., min_length=10, max_length=15)
    address: str = Field(..., min_length=10, max_length=255)
    city: str = Field(..., min_length=3, max_length=255)
    state: str = Field(..., min_length=3, max_length=255)
    zip: str = Field(..., min_length=5, max_length=10)
    country: str = Field(..., min_length=3, max_length=255) 
    role: str = Field(..., min_length=3, max_length=255)
   
class UserCreate(SQLModel):
    name: str = Field(..., min_length=3, max_length=255)
    email: EmailStr = Field(...)
    phone: str = Field(..., min_length=10, max_length=15)
    address: str = Field(..., min_length=10, max_length=255)
    city: str = Field(..., min_length=3, max_length=255)
    state: str = Field(..., min_length=3, max_length=255)
    zip: str = Field(..., min_length=5, max_length=10)
    country: str = Field(..., min_length=3, max_length=255)
    role: str = Field(..., min_length=3, max_length=255)
   
    
    
class UserUpdate(SQLModel):
    name: str = Field(..., min_length=3, max_length=255)
    email: EmailStr = Field(...)
    phone: str = Field(..., min_length=10, max_length=15)
    address: str = Field(..., min_length=10, max_length=255)
    city: str = Field(..., min_length=3, max_length=255)
    state: str = Field(..., min_length=3, max_length=255)
    zip: str = Field(..., min_length=5, max_length=10)
    country: str = Field(..., min_length=3, max_length=255)
    role: str = Field(..., min_length=3, max_length=255)
   
    
class UserView(AbstractDetailedView):
    name: str
    email: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    country: str
    role: str
