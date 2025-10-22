from enum import Enum


class BaseStatus(Enum):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    DELETED = "DELETED", "Deleted"
    
    def __init__(self, normal:str, label:str):
        self.normal = normal
        self.label = label
       