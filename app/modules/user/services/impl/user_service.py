from abc import ABC
from typing import Optional

from fastapi_pagination import Page
from sqlalchemy.testing.suite.test_reflection import users
from sqlmodel import Session

from app.common.enums import UserErrorCode, CommonErrorCode, BaseStatus
from app.common.exceptions import BasicExceptions
from app.common.models import PaginatedResponse
from app.modules.user.dao.user_dao import UserDao
from app.modules.user.mapper.user_mapper import UserMapper
from app.modules.user.misc import UserFilter
from app.modules.user.models import UserCreate, Users, UserView, UserUpdate
from app.modules.user.services.user_service_master import UserServiceMaster


class UserService(UserServiceMaster):



    def __init__(self):
        self.user_dao = UserDao()
        self.mapper = UserMapper()

    def create_user(self, session: Session, user: UserCreate) ->UserView:
        mapped_user= self.mapper.to_entity(user)
        print(f'mapped user: {mapped_user}')

        if mapped_user is None:
            BasicExceptions.raise_exception(
                CommonErrorCode.BAD_REQUEST,
                "Failed to map user data"
            )

        created_user = self.user_dao.save_user(session, mapped_user)
        return self.mapper.to_response(created_user)

    def get_user(self,session:Session,id:int) -> UserView:
        user:Users|None= self.user_dao.find_by_id(session,id)
        if user is None:
            BasicExceptions.raise_exception(UserErrorCode.USER_NOT_FOUND,"User not found")
            return None
        print(f'user: {user}')
        return self.mapper.to_response(user)

    def search_user(self, session: Session, filters: UserFilter) -> PaginatedResponse[UserView]:
        page_obj: Page[Users] = self.user_dao.search(session, filters)
        print(users)
        return PaginatedResponse.from_page(page_obj)

    
    def update_user(self, session: Session, id: int, user: UserUpdate) -> UserView:
        existing_user = self.user_dao.find_by_id(session,id)
        if existing_user is None:
            BasicExceptions.raise_exception(UserErrorCode.USER_NOT_FOUND,"User not found")
        updated_user = self.mapper.update_entity(existing_user,user)
        self.user_dao.save_user(session,updated_user)
        return self.mapper.to_response(updated_user)


    def delete_user(self, session: Session, id: int) -> bool:
        existing_user:Optional[Users] = self.user_dao.find_by_id( session, id)
        if existing_user is None:
            BasicExceptions.raise_exception(UserErrorCode.USER_NOT_FOUND,"User not found")
        if existing_user.status == BaseStatus.DELETED:
            BasicExceptions.raise_exception(UserErrorCode.USER_ALREADY_EXISTS,"User  is already deleted")
        existing_user.status  = BaseStatus.DELETED
        self.user_dao.save_user(session,existing_user)
        return True

