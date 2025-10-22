from app.global.shared.MapperConfig import MapperConfig
from py_automapper import AutoMapper
from app.modules.user.models.models import User, UserCreate, UserUpdate, UserView

mapper = AutoMapper()

mapper.add(UserCreate,
User,
ignore=MapperConfig.IGNORE_COMMON_FIELDS,
custom_mapping=MapperConfig.custom_for_creation()
)
mapper.add(User,
UserView,
ignore=MapperConfig.IGNORE_COMMON_FIELDS,
custom_mapping=MapperConfig.custom_for_view()
)

def map(user: UserCreate) -> User:
    return mapper.map(user, User)

def get_view(user: User) -> UserView:
    return mapper.map(user, UserView)

