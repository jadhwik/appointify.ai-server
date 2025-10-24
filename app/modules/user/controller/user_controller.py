from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.db import get_db
from app.modules.user.models import UserCreate, UserView
from app.modules.user.services.impl.user_service import UserService
from app.modules.user.services.user_service_master import UserServiceMaster


router = APIRouter(prefix="/users", tags=["users"])


# Dependency provider
def get_user_service() -> UserServiceMaster:
    return UserService()


@router.post("/")
def create_user(user: UserCreate,session: Session = Depends(get_db),user_service: UserServiceMaster = Depends(get_user_service)) ->UserView:
    return user_service.create_user(session, user)

@router.get("/{id}")
def get_user(id:int,session: Session = Depends(get_db),user_service: UserServiceMaster = Depends(get_user_service)):
    return user_service.get_user(session, id)

@router.delete("/{id}")
def delete_user(id:int,session:Session = Depends(get_db),user_service: UserServiceMaster = Depends(get_user_service)):
    return user_service.delete_user(session, id)




