from typing import Generic, TypeVar, Optional, Dict, Union, List, Any
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from fastapi_pagination import Page

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    code: int = 200
    message: str = "Success"
    data: Optional[Union[T, List[T], Any]] = None
    totalRecords: Optional[int] = None
    page: Optional[int] = None
    size: Optional[int] = None  # Changed from 'row' to 'size' to match fastapi-pagination
    pages: Optional[int] = None  # Changed from 'totalPages' to 'pages' to match fastapi-pagination
    details: Optional[Dict[str, str]] = None

    class Config:
        exclude_none = True

    @classmethod
    def of(cls, data: Union[T, Page[T], 'PaginatedResponse'], message: str = "Success"):
        """
        Unified factory method for regular, Page, and PaginatedResponse objects.
        Automatically detects the type and structures response accordingly.
        """
        from app.common.models.paginated_response_model import PaginatedResponse

        # Check if data is a PaginatedResponse object
        if isinstance(data, PaginatedResponse):
            instance = cls(
                code=200,
                message=message,
                data=data.data,
                totalRecords=data.totalRecords,
                page=data.page,
                size=data.size,
                pages=data.pages
            )
        # Check if data is a Page object
        elif isinstance(data, Page):
            instance = cls(
                code=200,
                message=message,
                data=data.items,
                totalRecords=data.total,
                page=data.page,
                size=data.size,
                pages=data.pages
            )
        else:
            # Regular response - don't set pagination fields at all
            instance = cls(code=200, message=message, data=data)

        # Return JSONResponse with exclude_none=True
        return JSONResponse(
            status_code=200,
            content=jsonable_encoder(instance, exclude_none=True)
        )

    @classmethod
    def from_exception(cls, e: Exception):
        if hasattr(e, "code"):
            code = getattr(e, "code")
        else:
            code = 500

        message = str(e)
        status_code = (
            status.HTTP_401_UNAUTHORIZED if "auth" in message.lower()
            else status.HTTP_404_NOT_FOUND if "not found" in message.lower()
            else status.HTTP_400_BAD_REQUEST if code == 400
            else status.HTTP_500_INTERNAL_SERVER_ERROR
        )

        return JSONResponse(
            status_code=status_code,
            content=jsonable_encoder(
                cls(code=code, message=message, data=None),
                exclude_none=True
            )
        )