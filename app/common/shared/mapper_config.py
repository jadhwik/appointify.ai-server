from datetime import datetime

from app.common.enums import BaseStatus


class MapperConfig:
    IGNORE_COMMON_FIELDS = ["id", "version", "createdOn", "updatedOn", "status"]
     
    @staticmethod
    def custom_for_creation():
         return {
           "createdOn": lambda _: datetime.utcnow(),
            "updatedOn": lambda _: datetime.utcnow(),
            "version": lambda _: 0,
             "status": lambda _: BaseStatus.ACTIVE,
        }
    
    @staticmethod
    def custom_for_view():
        return {
            "created_on": lambda user: user.created_on,  # use snake_case
            "updated_on": lambda user: user.updated_on,  # use snake_case
            "version": lambda user: user.version,
            "status": lambda user: user.status,
        }
        