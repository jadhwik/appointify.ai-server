from typing import Optional, List

from pydantic import BaseModel, conint

from app.common.enums.base_status import base_status


class DateFilter():
    field: Optional[str] = None
    from_date: Optional[int] = None
    to_date: Optional[int] = None



class BaseFilter(BaseModel):
    status: Optional[List[base_status]] = None
    # Pagination
    page: conint(ge=0) = 0
    rows: conint(ge=1, le=1000) = 15

    # Search query
    query: Optional[str] = None

    # Sorting
    sort_by: Optional[str] = "created_on"
    sort_in: Optional[str] = "desc"  # "asc" or "desc"

    # Timezone
    timezone: Optional[str] = None

    # Custom getter for status default
    @property
    def get_status(self) -> List[base_status]:
        return self.status or [base_status.ACTIVE]

    # Custom getter for timezone default
    @property
    def get_timezone(self, pytz=None) -> str:
        return self.timezone or str(pytz.timezone("UTC"))

    # Helper method for sorting direction
    @property
    def is_ascending(self) -> bool:
        return self.sort_in.lower() == "asc"

    # Helper method for SQLAlchemy offset & limit
    @property
    def offset(self) -> int:
        return self.page * self.rows

    @property
    def limit(self) -> int:
        return self.rows
