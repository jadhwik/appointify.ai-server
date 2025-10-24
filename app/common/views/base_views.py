from datetime import datetime
from sqlmodel import SQLModel, Field
from typing import Optional

from app.common.enums import BaseStatus


class AbstractBasicView(SQLModel):
    id: Optional[int] = None
    version: Optional[int] = None


class AbstractDetailedView(AbstractBasicView):
    created_on: datetime = Field(alias="createdOn")
    updated_on: datetime = Field(alias="updatedOn")
    status: BaseStatus

    class Config:
        allow_population_by_field_name = True
