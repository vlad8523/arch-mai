import secrets

import os
from pydantic import computed_field



class AppSettings():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ALGORITHM = 'HS256'

    mongo_uri: str = os.getenv("MONGO_URI")
    mongo_db: str = os.getenv("MONGO_DB")