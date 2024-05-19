from fastapi import APIRouter, Depends, HTTPException, status

from api.dependencies.postgres_repository import get_repository
from core.security import verify_password
from db.repositories.user import UserRepository
from models.domain.user import UserLogin

router = APIRouter()


@router.post('/')
async def login(
    user_form: UserLogin,
    repository: UserRepository = Depends(get_repository(UserRepository))
):
    print(user_form.model_dump_json())

    user_in_db = await repository.get_user_by_email(user_form.email)
    
    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found with this username.'
        )

    user_in_db = user_in_db[0]

    verified = verify_password(user_form.password, user_in_db.hashed_password)
    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Password is wrong.'
        )
    
    return user_in_db