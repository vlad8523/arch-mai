# from datetime import timedelta

# from fastapi import APIRouter, Depends, HTTPException

# from models.user import UserLogin
# from models.misc import Token
# from app.core.db import get_db
# from app.core import security
# from app.core.security import settings

# from app import crud

# router = APIRouter()

# @router.post("")
# def login(
#     user_in: UserLogin,
#     session=Depends(get_db)):
#     user = crud.authentificate(email=user_in.email, password=user_in.password, session=session)
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect email or password")
#     access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     return Token(
#         access_token=security.create_access_token(
#             user.id, expires_delta=access_token_expires
#         )
#     )