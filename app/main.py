from fastapi import FastAPI
from app.core.db import create_db_and_tables
from app.modules.user.controller.user_controller import router as user_router  # import the router

app = FastAPI(
    title="Appointify AI API",
    description="API documentation for Appointify.AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Create tables at startup
create_db_and_tables()

# Include the user router
app.include_router(user_router)
