from abc import abstractmethod

from sqlmodel import Session

from app.modules.user.models import UserCreate


class UserServiceMaster:

    @abstractmethod
    def createUser(self,session:Session, user:UserCreate):
        pass

