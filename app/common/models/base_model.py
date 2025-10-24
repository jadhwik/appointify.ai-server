from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional
from app.common.enums.base_status import BaseStatus
from sqlalchemy import Column, String

class AbstractBaseModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    version: int = Field(default=0)


class AbstractTransactionalModel(AbstractBaseModel):
    created_on: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
    updated_on: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False
    )
    status: BaseStatus = Field(
        sa_column=Column(String, default=BaseStatus.ACTIVE.value, nullable=False)
    )
