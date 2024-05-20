import aiohttp
from fastapi import APIRouter, status, HTTPException, Request, Response

from models.users import UserCreate, UserResponse
from config import settings
from network import make_request


router = APIRouter()


@router.post("/")
async def create_user(
    user_new: UserCreate,
    request: Request, response: Response
) -> UserResponse | None:
    scope = request.scope

    method = scope['method'].lower()
    path = scope['path']
    
    url = f'{settings.USERS_SERVICE_URL}{path}'

    payload = user_new.model_dump() if user_new else {}

    try: 
        resp_data, status_code = await make_request(
            url=url,
            method=method,
            data=payload,
        )
    except aiohttp.client_exceptions.ClientConnectorError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail='Service is unavailable.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    except aiohttp.client_exceptions.ContentTypeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Service error.',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    
    response.status_code = status_code
    if status_code == status.HTTP_200_OK:
        return resp_data
    else:
        raise HTTPException(
            status_code=status_code,
            detail=resp_data["detail"]
        )


@router.get("/{user_id}")
async def get_user(    
    user_id: int,
    request: Request, response: Response
) -> None:
    print(f"authorization token: {request.headers.get("Authorization")}")


# @router.get("/")
# async def get_user_by_name(
#     user_search: UserSearch,
#     repository: UserRepository = Depends(get_repository(UserRepository))
# ):
#     users = await repository.get_users_by_first_and_second_name(first_name=user_search.first_name,
#                                                                 second_name=user_search.second_name)

#     if not users:
#         raise HTTPException(
#             status_code=400,
#             detail="No users with this name."
#         )
    
#     return users


# @router.patch("/{user_id}")
# async def update_user(
#     user_id: int, 
#     user_data: UserCreate,
#     repository: UserRepository = Depends(get_repository(UserRepository))
# ) -> UserInDB | None:
#     user = await repository.read_by_id(user_id)

#     if user is None: 
#         return HTTPException(
#             status_code=400,
#             detail="User not found"
#         )
    
#     await repository.update_user(user_id, user_data)

#     return await repository.read_by_id(user_id)


# @router.delete("/{user_id}")
# async def delete_user(
#     user_id: int, 
#     repository: UserRepository = Depends(get_repository(UserRepository))
# ) -> UserInDB | None:
#     user = await repository.delete(user_id)

#     if not user: 
#         raise HTTPException(
#             status_code=400, detail="User not found"
#         )
    
#     return user