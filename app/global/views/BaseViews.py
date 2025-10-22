from sqlmodel import SQLModel
from datetime import datetime
from app.global.enums.BaseStatus import BaseStatus
from typing import Optional

class AbstractBasicView(SQLModel):
    id: Optional[int] = None
    version: Optional[int] = None
    
class AbstractDetailedView(AbstractBasicView):
    createdOn: Optional[datetime] = None
    updatedOn: Optional[datetime] = None
    status: Optional[BaseStatus] = None
