from fastapi import APIRouter

from api.routes import users, login

api_router = APIRouter()
api_router.include_router(users.router, prefix='/user')
api_router.include_router(login.router, prefix='/login')