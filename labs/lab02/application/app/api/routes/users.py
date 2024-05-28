from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies.postgres_repository import get_repository
from app.db.repositories.user import UserRepository
from app.models.domain.user import UserCreate, UserInDB

from db_fill import test_data


router = APIRouter()

@router.post("/")
async def create_user(
    user_new: UserCreate,
    repository: UserRepository = Depends(get_repository(UserRepository))
) -> UserInDB | None:
    print(user_new.model_dump())
    
    existed_user = await repository.get_user_by_email(user_new.email)
    
    if existed_user:
        print(existed_user)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email is exist."
        )
    
    existed_user = await repository.get_user_by_username(user_new.username)
    
    if existed_user:
        print(existed_user)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this username is exist."
        )
    
    user = await repository.create(obj_new=user_new)
    print(user)
    return user


@router.get("/{user_id}")
async def get_user(
    user_id: int, 
    repository: UserRepository = Depends(get_repository(UserRepository))
) -> UserInDB | None:
    user = await repository.read_by_id(user_id)
    
    if not user:
        raise HTTPException(
            status_code=400,
            detail="No user with this id.",
        )
    
    return user


@router.patch("/{user_id}")
async def update_user(
    user_id: int, 
    user_data: UserCreate,
    repository: UserRepository = Depends(get_repository(UserRepository))
) -> UserInDB | None:
    user = await repository.read_by_id(user_id)

    if user is None: 
        return HTTPException(
            status_code=400,
            detail="User not found"
        )
    
    await repository.update_user(user_id, user_data)

    return await repository.read_by_id(user_id)


@router.delete("/{user_id}")
async def delete_user(
    user_id: int, 
    repository: UserRepository = Depends(get_repository(UserRepository))
) -> UserInDB | None:
    user = await repository.delete(user_id)

    if not user: 
        raise HTTPException(
            status_code=400, detail="User not found"
        )
    
    return user


@router.post("/test-data")
async def create_test_data(
    repository: UserRepository = Depends(get_repository(UserRepository))
):
    users: List[UserInDB] = []
    for user_new in test_data:
        try:
            users.append(await create_user(user_new=user_new,
                                       repository=repository))
        except HTTPException as e:
            raise e

    return users