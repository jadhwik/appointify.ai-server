from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

# Create PostgreSQL engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)

def create_db_and_tables():
    """Create all SQLModel tables"""
    SQLModel.metadata.create_all(engine)

def get_db():
    """Dependency to get PostgreSQL session"""
    with Session(engine) as session:
        yield session