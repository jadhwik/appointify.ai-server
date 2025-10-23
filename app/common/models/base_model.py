from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

from app.common.enums.base_status import BaseStatus


class AbstractBaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    version: Optional[int] = Field(default=None)


class AbstractTransactionalModel(AbstractBaseModel):
    createdOn: Optional[datetime] = Field(default=None)
    updatedOn: Optional[datetime] = Field(default=None)
    status: Optional[BaseStatus] = Field(default=BaseStatus.ACTIVE)
