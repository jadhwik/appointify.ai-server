from fastapi import FastAPI, Request, HTTPException, APIRouter
from fastapi.responses import JSONResponse
from fastapi_pagination import add_pagination

from app.common.models import ResponseModel
from app.core.config import Settings
from app.core.db import create_db_and_tables
from app.modules.user.controller.user_controller import router as user_router


settings = Settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="API documentation for Appointify.AI",
    version="1.0.0",
    prefix="/api",
    docs_url="/docs",
    redoc_url="/redoc"
)

api_router = APIRouter(prefix="/api")
api_router.include_router(user_router)

app.include_router(api_router)

add_pagination(app)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    response = ResponseModel(
        code=exc.detail.get("status", exc.status_code),
        message=exc.detail.get("message", "Error"),
        data=None
    )
    return JSONResponse(status_code=exc.status_code, content=response.dict())

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
