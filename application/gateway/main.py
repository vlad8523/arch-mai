from fastapi import FastAPI, status

from config import settings
from core import route

app = FastAPI

@route(
    request_method=app.post,
    path='/api/login',
    status_code=status.HTTP_201_CREATED,
    payload_key='username_password',
    service_url=settings.USERS_SERVICE_URL,
    authentication_required=False,
    post_processing_func='post_processing.access_token_generate_handler',
    response_model='datastructures.users.LoginResponse'
)
async def login():
    pass