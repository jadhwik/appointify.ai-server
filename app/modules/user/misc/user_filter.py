from typing import Optional

from app.common.misc.base_filter import BaseFilter


class UserFilter(BaseFilter):
    name: Optional[str] = None
    phone: Optional[str] = None