from datetime import datetime
from sqlmodel import SQLModel
from typing import Optional

from app.common.enums import BaseStatus


class AbstractBasicView(SQLModel):
    id: Optional[int] = None
    version: Optional[int] = None


class AbstractDetailedView(AbstractBasicView):
    createdOn: Optional[datetime] = None
    updatedOn: Optional[datetime] = None
    status: Optional[BaseStatus] = None
