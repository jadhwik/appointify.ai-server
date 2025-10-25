from fastapi_pagination import Page
from typing import TypeVar, Generic, List
from pydantic import BaseModel

T = TypeVar('T')


class PaginatedResponse(BaseModel, Generic[T]):
    data: List[T]
    totalRecords: int
    page: int
    size: int  # Changed from 'row' to 'size'
    pages: int  # Changed from 'totalPages' to 'pages'

    @classmethod
    def from_page(cls, page_obj: Page[T]) -> 'PaginatedResponse[T]':
        return cls(
            data=page_obj.items,
            totalRecords=page_obj.total,
            page=page_obj.page,
            size=page_obj.size,
            pages=page_obj.pages
        )