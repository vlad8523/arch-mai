from fastapi import APIRouter

from api.routes import routes


api_router = APIRouter()

api_router.include_router(routes.router, prefix="/route")
