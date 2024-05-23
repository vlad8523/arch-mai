from fastapi import FastAPI

from api.main import api_router
from handlers.event_handlers import startup


app = FastAPI()

app.include_router(api_router, prefix="/api")
app.add_event_handler("startup", startup)