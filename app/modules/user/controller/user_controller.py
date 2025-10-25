from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.common.models import ResponseModel, PaginatedResponse
from app.core.db import get_db
from app.modules.user.misc import UserFilter
from app.modules.user.models import UserCreate, UserView
from app.modules.user.services.impl.user_service import UserService
from app.modules.user.services.user_service_master import UserServiceMaster


router = APIRouter(prefix="/users", tags=["users"])


# Dependency provider
def get_user_service() -> UserServiceMaster:
    return UserService()


@router.post("/",response_model=ResponseModel[UserView])
def create_user(user: UserCreate,session: Session = Depends(get_db),user_service: UserServiceMaster = Depends(get_user_service)) ->UserView:
    user_view = user_service.create_user(session, user)
    return ResponseModel.of(user_view)

@router.get("/{id}",response_model=ResponseModel[UserView])
def get_user(id:int,session: Session = Depends(get_db),user_service: UserServiceMaster = Depends(get_user_service)):
    user_view = user_service.get_user(session, id)
    return  ResponseModel.of(user_view)

@router.post("/search")
def search_users(filters:UserFilter,session:Session = Depends(get_db),user_service: UserServiceMaster = Depends(get_user_service)):
    users = user_service.search_user(session, filters)
    return ResponseModel.of(users)

@router.delete("/{id}")
def delete_user(id:int,session:Session = Depends(get_db),user_service: UserServiceMaster = Depends(get_user_service)):
    return user_service.delete_user(session, id)




