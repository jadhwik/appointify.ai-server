from abc import abstractmethod, ABC

from sqlmodel import Session

from app.modules.user.models import UserCreate, UserView, UserUpdate


class UserServiceMaster(ABC):

    @abstractmethod
    def create_user(self, session: Session, user: UserCreate) -> UserView:
        """Create a new user"""
        pass

    @abstractmethod
    def get_user(self, session: Session, id: int) ->UserView:
        """Get user by ID"""
        pass

    @abstractmethod
    def update_user(self, session: Session, id: int, user: UserUpdate) -> UserView:
        """Update existing user"""
        pass

    @abstractmethod
    def delete_user(self, session: Session, id: int) -> bool:
        """Delete user by ID"""
        pass

