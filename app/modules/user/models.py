from sqlmodel import SQLModel, Field, create_engine, Session, select

# Define a model
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str

# Database connection
engine = create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

# CRUD operations
with Session(engine) as session:
    user = User(name="Alice", email="alice@example.com")
    session.add(user)
    session.commit()
