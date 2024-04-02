from fastapi import FastAPI
from fastapi.routing import APIRoute

from api.main import api_router
from core.db import connect

from core.config import settings

app = FastAPI(
    title="BlaBla lab",
)

app.include_router(api_router, prefix=settings.API_V1_STR)
app.add_event_handler("startup", connect)