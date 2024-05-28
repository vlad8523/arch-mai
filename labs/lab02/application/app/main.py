from fastapi import FastAPI
from fastapi.routing import APIRoute

from app.api.main import api_router
from app.handlers.event_handlers import startup
from app.core.config import get_app_settings

app = FastAPI(
    title="BlaBla lab",
)

settings = get_app_settings()

app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_event_handler("startup", startup)