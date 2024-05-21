import secrets

import os
from pydantic import computed_field



class AppSettings():
    mongo_uri: str = os.getenv("MONGO_URI")
    mongo_db: str = os.getenv("MONGO_DB")