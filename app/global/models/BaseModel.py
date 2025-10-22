from datetime import datetime
from app.global.enums.BaseStatus import BaseStatus
from sqlmodel import SQLModel, Field
from typing import Optional


class AbstractBaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    version: Optional[int] = Field(default=None)


class AbstractTransactionalModel(AbstractBaseModel):
    createdOn: Optional[datetime] = Field(default=None)
    updatedOn: Optional[datetime] = Field(default=None)
    status: Optional[BaseStatus] = Field(default=BaseStatus.ACTIVE)
