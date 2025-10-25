from fastapi import HTTPException
from app.common.enums import UserErrorCode


class BasicExceptions:
    @staticmethod
    def raise_exception(error_code_enum, message: str = None):
        """
        Generic exception raiser for all modules.

        :param error_code_enum: Enum item (e.g. UserErrorCode.USER_NOT_FOUND)
        :param message: Optional custom message override
        """
        raise HTTPException(
            status_code=error_code_enum.http_status,
            detail={
                "error_code": error_code_enum.message,
                "status": error_code_enum.code,
                "message": message or error_code_enum.message
            }
        )
