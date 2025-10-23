
from py_automapper import AutoMapper

from app.common.shared.mapper_config import MapperConfig
from app.modules.user.models import UserCreate,Users,UserUpdate,UserView

mapper = AutoMapper()

class UserMapper:
    mapper.add(UserCreate,
               Users,
               ignore=MapperConfig.IGNORE_COMMON_FIELDS,
               custom_mapping=MapperConfig.custom_for_creation()
               )
    mapper.add(Users,
               UserView,
               ignore=MapperConfig.IGNORE_COMMON_FIELDS,
               custom_mapping=MapperConfig.custom_for_view()
               )
    @property
    def get_entity(user: UserCreate) -> Users:
        return mapper.map(user, Users)

    @property
    def get_view(user: Users) -> UserView:
        return mapper.map(user, UserView)




