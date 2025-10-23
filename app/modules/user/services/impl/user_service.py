from sqlmodel import Session

from app.common.enums import UserErrorCode, CommonErrorCode
from app.common.exceptions import BasicExceptions
from app.modules.user.dao.user_dao import UserDao
from app.modules.user.mapper.user_mapper import UserMapper
from app.modules.user.models import UserCreate,Users
from app.modules.user.services.user_service_master import UserServiceMaster


class UserService(UserServiceMaster):

    def __init__(self):
        # Use snake_case and remove semicolons
        self.user_dao = UserDao()
        self.user_mapper = UserMapper()

    def create_user(self, session: Session, user: UserCreate):
        mapped_user: Users = self.user_mapper.get_entity
        if mapped_user is None:
            BasicExceptions.raise_exception(CommonErrorCode.BAD_REQUEST,"Empty Data")
        self.user_dao.save_user(session, mapped_user)
        return self.user_mapper.get_view

    def get_user(self,session:Session,id:int):
        user:Users|None= self.user_dao.find_by_id(self,session,id)
        if user is None:
            BasicExceptions.raise_exception(CommonErrorCode.NOT_FOUND,"User not found")
            return None
        return self.user_mapper.get_view



