from fastapi import APIRouter

from app.db.mongodb import db_client

router = APIRouter()

@router.post("")
async def create_route():
    print(db_client)