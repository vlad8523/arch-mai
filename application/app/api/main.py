from fastapi import APIRouter

from app.api.routes import users
from app.api.routes import routes

api_router = APIRouter()
api_router.include_router(users.router, prefix='/user')
api_router.include_router(routes.router, prefix='/route')
# api_router.include_router(login.router, prefix='/login')