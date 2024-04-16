# from typing import Any

# from fastapi import APIRouter, Depends, HTTPException

# from app.core.db import get_db
# from app.core.security import verify_password

# from app.db.models.user import UserCreate, User, UserSearchFirstSecondName, UserUpdateMe, UserLogin

# from 
# from app.db.models.misc import Message

# from app import crud

# router = APIRouter()


# @router.post("/")
# def create_user(user_in: UserCreate, session=Depends(get_db)):
#     user = crud.get_user_by_email(session=session, email=user_in.email)
#     if user:
#         raise HTTPException(
#             status_code=400,
#             detail="The user with this email already exists in the system.",
#         )

#     user = crud.create_user(session=session, user_create=user_in)
    
#     return user


# @router.get("/{user_id}")
# def get_user(user_id: int, 
#              session=Depends(get_db)):
#     user = crud.get_user_by_id(session=session, id=user_id)
    
#     if not user:
#         raise HTTPException(
#             status_code=400,
#             detail="No user with this id.",
#         )
    
#     return user


# @router.get("/search")
# def get_user_by_name(user_search: UserSearchFirstSecondName, session=Depends(get_db)):
#     users = crud.search_user(session=session,
#                              user_search=user_search)
    
#     return users


# @router.patch("/{user_id}")
# def update_user(
#     *,
#     user_id: int,
#     user_in: UserUpdateMe,
#     session=Depends(get_db)
# ) -> Any:
#     db_user = session.get(User, user_id)
#     if not db_user:
#         raise HTTPException(
#             status_code=400,
#             detail="No user with this id.",
#         )
    
#     if user_in.email:
#         existing_user = crud.get_user_by_email(session=session, email=user_in.email)
#         if existing_user and existing_user.id != user_id:
#             raise HTTPException(
#                 status_code=409, detail="User with this email already exists"
#             )
        
    
#     db_user = crud.update_user(session=session, db_user=db_user, user_in=user_in)


from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies.postgres_repository import get_repository
from app.db.repositories.user import UserRepository
from app.models.domain.user import UserInDB, UserCreate, UserBase

router = APIRouter()


@router.post("/", response_model=UserInDB)
async def create_user(
    user_new: UserBase,
    repository: UserRepository = Depends(get_repository(UserRepository))
) -> UserInDB | None:
    existed_user = await repository.get_user_by_email(user_new.email)

    if existed_user:
        print(existed_user)
        raise HTTPException(
            status_code=409,
            detail="User with this email is exist"
        )


    user = await repository.create(obj_new=user_new)
    
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