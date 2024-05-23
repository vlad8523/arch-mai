from fastapi import FastAPI, Request, Response, status

from config import settings
from core import route
from models.users import UserLogin
from api.main import api_router

from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(api_router, prefix='/api')