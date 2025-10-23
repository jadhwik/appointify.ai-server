from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.core.db import get_db
from app.modules.user.models import UserCreate
from app.modules.user.services.user_service_master import UserServiceMaster
  # Make sure this returns a SQLModel session

router = APIRouter(prefix="/users", tags=["users"])


# Dependency provider
def get_user_service() -> UserServiceMaster:
    return UserServiceMaster()


@router.post("/")
def create_user(user: UserCreate,session: Session = Depends(get_db()),user_service: UserServiceMaster = Depends(get_user_service)):
    return user_service.create(session, user)
