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


# @router.delete("/{user_id}")
# def delete_user(
#     user_id: int,
#     user_login: UserLogin,
#     session=Depends(get_db)) -> Any:

#     user = session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     elif user.email != user_login.email or not verify_password(user_login.password, user.hashed_password):
#         print(user.email, user_login.email)
#         raise HTTPException(
#             status_code=403, detail="Wrong email or password"
#         )

#     session.delete(user)
#     session.commit()
#     return Message(message="User deleted successfully")


from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.api.de