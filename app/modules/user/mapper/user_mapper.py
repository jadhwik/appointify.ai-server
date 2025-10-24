from app.common.mapper.base_mapper import BaseMapper
from app.modules.user.models import UserCreate, UserUpdate, Users, UserView


class UserMapper(BaseMapper[UserCreate,Users,UserView]):
    def __init__(self):
        super().__init__(UserCreate,Users,UserView)

