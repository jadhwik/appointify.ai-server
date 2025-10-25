from typing import TypeVar, Generic, Type, Optional, List, Dict, Any, Tuple
from sqlmodel import Session, select, SQLModel, col
from sqlalchemy import func, asc, desc

from app.common.criteria import BaseCriteria

T = TypeVar("T", bound=SQLModel)


class BasicDao(BaseCriteria, Generic[T]):
    """
    Base Data Access Object implementing common CRUD operations.
    Similar to Spring Data JPA Repository pattern.
    """

    def __init__(self, model: Type[T]):
        self.model = model

    # CREATE
    def save(self, session: Session, obj: T) -> T:
        """Save a single entity."""
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def save_all(self, session: Session, objs: List[T]) -> List[T]:
        """Save multiple entities in batch."""
        session.add_all(objs)
        session.commit()
        for obj in objs:
            session.refresh(obj)
        return objs

    # READ
    def find_by_id(self, session: Session, id: int) -> Optional[T]:
        """Find entity by ID."""
        return session.get(self.model, id)

    def exists_by_id(self, session: Session, id: int) -> bool:
        """Check if entity exists by ID."""
        return session.get(self.model, id) is not None

    def find_all(self, session: Session) -> List[T]:
        """Find all entities."""
        return session.exec(select(self.model)).all()

    def find_all_by_ids(self, session: Session, ids: List[int]) -> List[T]:
        """Find all entities by list of IDs."""
        return session.exec(
            select(self.model).where(self.model.id.in_(ids))
        ).all()

    def count(self, session: Session) -> int:
        """Count all entities."""
        return session.exec(
            select(func.count()).select_from(self.model)
        ).one()

    # UPDATE
    def update(self, session: Session, obj: T, updates: Dict[str, Any]) -> T:
        """Update entity with provided fields."""
        for key, value in updates.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        if hasattr(obj, 'updatedOn'):
            obj.updatedOn = func.now()

        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def update_by_id(self, session: Session, id: int, updates: Dict[str, Any]) -> Optional[T]:
        """Find and update entity by ID."""
        obj = self.find_by_id(session, id)
        if not obj:
            return None
        return self.update(session, obj, updates)

    # DELETE
    def delete(self, session: Session, obj: T) -> None:
        """Hard delete an entity."""
        session.delete(obj)
        session.commit()

    def delete_by_id(self, session: Session, id: int) -> bool:
        """Hard delete entity by ID."""
        obj = self.find_by_id(session, id)
        if not obj:
            return False
        session.delete(obj)
        session.commit()
        return True

    def soft_delete(self, session: Session, obj: T) -> T:
        """Soft delete by setting status to DELETED."""
        if hasattr(obj, 'status'):
            obj.status = "DELETED"
        if hasattr(obj, 'updatedOn'):
            obj.updatedOn = func.now()

        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def soft_delete_by_id(self, session: Session, id: int) -> bool:
        """Soft delete entity by ID."""
        obj = self.find_by_id(session, id)
        if not obj:
            return False
        self.soft_delete(session, obj)
        return True



    # CUSTOM QUERY METHODS
    def find_one_by(self, session: Session, **filters) -> Optional[T]:
        """Find single entity by field values."""
        query = select(self.model)
        for key, value in filters.items():
            if hasattr(self.model, key):
                query = query.where(getattr(self.model, key) == value)
        return session.exec(query).first()

    def find_all_by(self, session: Session, **filters) -> List[T]:
        """Find all entities by field values."""
        query = select(self.model)
        for key, value in filters.items():
            if hasattr(self.model, key):
                query = query.where(getattr(self.model, key) == value)
        return session.exec(query).all()

    def count_by(self, session: Session, **filters) -> int:
        """Count entities by field values."""
        query = select(func.count()).select_from(self.model)
        for key, value in filters.items():
            if hasattr(self.model, key):
                query = query.where(getattr(self.model, key) == value)
        return session.exec(query).one()


