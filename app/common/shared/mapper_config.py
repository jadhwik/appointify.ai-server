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
           "createdOn": lambda user: user.createdOn,
            "updatedOn": lambda user: user.updatedOn,
            "version": lambda user: user.version,
             "status": lambda user: user.status,
        }
        