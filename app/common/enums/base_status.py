from enum import Enum


class BaseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETED = "DELETED"

    @property
    def label(self) -> str:
        """Get user-friendly label for the status."""
        labels = {
            "ACTIVE": "Active",
            "INACTIVE": "Inactive",
            "DELETED": "Deleted"
        }
        return labels.get(self.value, self.value)

    @classmethod
    def get_active_statuses(cls) -> list['BaseStatus']:
        return [cls.ACTIVE, cls.INACTIVE]
