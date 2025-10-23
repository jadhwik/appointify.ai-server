from datetime import datetime
from sqlmodel import SQLModel
from typing import Optional

from app.common.enums import BaseStatus


class abstract_basic_view(SQLModel):
    id: Optional[int] = None
    version: Optional[int] = None


class abstarct_detailed_view(abstract_basic_view):
    createdOn: Optional[datetime] = None
    updatedOn: Optional[datetime] = None
    status: Optional[BaseStatus] = None
