from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies.postgres_repository import get_repository
from db.repositories.user import UserRepository
from models.domain.user import UserCreate, UserInDB


router = APIRouter()

@router.post("/")
async def create_user(
    user_new: UserCreate,
    repository: UserRepository = Depends(get_repository(UserRepository))
) -> UserInDB | None:
    existed_user = await repository.get_users_by_email(user_new.email)
    
    if existed_user:
        print(existed_user)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email is exist."
        )
    
    user = await repository.create(obj_new=user_new)

    return user