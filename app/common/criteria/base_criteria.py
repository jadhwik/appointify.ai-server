from sqlmodel import select
from sqlalchemy.sql import and_, or_
from typing import Any, Type, List, Optional
from sqlmodel import SQLModel


class BaseCriteria:
    def __init__(self, model: Type[SQLModel]):
        self.model = model
        self.filters = []

    def eq(self, field_name: str, value: Any):
        """Add equals condition only if value is not None"""
        if value is not None:
            self.filters.append(getattr(self.model, field_name) == value)
        return self

    def ne(self, field_name: str, value: Any):
        """Add not equals condition only if value is not None"""
        if value is not None:
            self.filters.append(getattr(self.model, field_name) != value)
        return self

    def like(self, field_name: str, value: str):
        """Add LIKE condition only if value exists"""
        if value:
            self.filters.append(getattr(self.model, field_name).like(f"%{value}%"))
        return self

    def ilike(self, field_name: str, value: str):
        """Case-insensitive LIKE, only if value exists"""
        if value:
            self.filters.append(getattr(self.model, field_name).ilike(f"%{value}%"))
        return self

    def starts_with(self, field_name: str, value: str):
        """Add LIKE 'value%' condition only if value exists"""
        if value:
            self.filters.append(getattr(self.model, field_name).like(f"{value}%"))
        return self

    def ends_with(self, field_name: str, value: str):
        """Add LIKE '%value' condition only if value exists"""
        if value:
            self.filters.append(getattr(self.model, field_name).like(f"%{value}"))
        return self

    def gt(self, field_name: str, value: Any):
        """Add greater than condition only if value is not None"""
        if value is not None:
            self.filters.append(getattr(self.model, field_name) > value)
        return self

    def gte(self, field_name: str, value: Any):
        """Add greater than or equal condition only if value is not None"""
        if value is not None:
            self.filters.append(getattr(self.model, field_name) >= value)
        return self

    def lt(self, field_name: str, value: Any):
        """Add less than condition only if value is not None"""
        if value is not None:
            self.filters.append(getattr(self.model, field_name) < value)
        return self

    def lte(self, field_name: str, value: Any):
        """Add less than or equal condition only if value is not None"""
        if value is not None:
            self.filters.append(getattr(self.model, field_name) <= value)
        return self

    def in_(self, field_name: str, values: Optional[List]):
        """Add IN condition only if values list is not empty"""
        if values:
            self.filters.append(getattr(self.model, field_name).in_(values))
        return self

    def not_in(self, field_name: str, values: Optional[List]):
        """Add NOT IN condition only if values list is not empty"""
        if values:
            self.filters.append(~getattr(self.model, field_name).in_(values))
        return self

    def between(self, field_name: str, start: Any, end: Any):
        """Add BETWEEN condition only if both start and end exist"""
        if start is not None and end is not None:
            self.filters.append(getattr(self.model, field_name).between(start, end))
        return self

    def is_null(self, field_name: str, condition: bool = True):
        """Add IS NULL condition only if condition is True"""
        if condition:
            self.filters.append(getattr(self.model, field_name).is_(None))
        return self

    def is_not_null(self, field_name: str, condition: bool = True):
        """Add IS NOT NULL condition only if condition is True"""
        if condition:
            self.filters.append(getattr(self.model, field_name).isnot(None))
        return self

    def build(self):
        """Return a SQLModel Select query with filters applied. Empty filters = select all."""
        query = select(self.model)
        if self.filters:
            query = query.where(and_(*self.filters))
        return query