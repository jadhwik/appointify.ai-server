from sqlmodel import select
from sqlalchemy.sql import and_
from typing import Any, Type
from sqlmodel import SQLModel


class BaseFilter:
    def __init__(self, model: Type[SQLModel]):
        self.model = model
        self.filters = []

    def eq(self, field_name: str, value: Any):
        if value is not None:
            self.filters.append(getattr(self.model, field_name) == value)
        return self

    def like(self, field_name: str, value: str):
        if value:
            self.filters.append(getattr(self.model, field_name).like(f"%{value}%"))
        return self

    def gt(self, field_name: str, value: Any):
        if value is not None:
            self.filters.append(getattr(self.model, field_name) > value)
        return self

    def gte(self, field_name: str, value: Any):
        if value is not None:
            self.filters.append(getattr(self.model, field_name) >= value)
        return self

    def lt(self, field_name: str, value: Any):
        if value is not None:
            self.filters.append(getattr(self.model, field_name) < value)
        return self

    def lte(self, field_name: str, value: Any):
        if value is not None:
            self.filters.append(getattr(self.model, field_name) <= value)
        return self

    def in_(self, field_name: str, values: list):
        if values:
            self.filters.append(getattr(self.model, field_name).in_(values))
        return self

    def between(self, field_name: str, start: Any, end: Any):
        if start and end:
            self.filters.append(getattr(self.model, field_name).between(start, end))
        return self

    def build(self):
        """Return a SQLModel Select query with filters applied."""
        query = select(self.model)
        if self.filters:
            query = query.where(and_(*self.filters))
        return query
