from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies.postgres_repository import get_repository
from core.security import verify_password
from db.models import user
from db.repositories.user import UserRepository
from models.domain.user import UserInDB, UserLogin
from security.auth import generate_access_token

router = APIRouter()


@router.post('/')
async def login(
    user_form: UserLogin,
    repository: UserRepository = Depends(get_repository(UserRepository))
) -> str:
    print(user_form.model_dump_json())

    user_in_db = await repository.get_user_by_username(user_form.username)
    
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found with this username.'
        )
    
    print(user_in_db)

    verified = verify_password(user_form.password, user_in_db.hashed_password)
    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Password is wrong.'
        )
    
    data = user_in_db.__dict__

    del data["_sa_instance_state"]

    print(user_in_db)
    print(UserInDB(**data))

    
    return generate_access_token(UserInDB(**data).model_dump())