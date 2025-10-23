from abc import abstractmethod

from sqlmodel import Session

from app.modules.user.models import UserCreate


class UserServiceMaster:

    @abstractmethod
    def create_user(self,session:Session, user:UserCreate):
        pass

