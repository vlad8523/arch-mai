from fastapi import FastAPI, Request, Response, status

from config import settings
from core import route
from models.users import UserLogin
from api.main import api_router

app = FastAPI()

app.include_router(api_router, prefix='/api')