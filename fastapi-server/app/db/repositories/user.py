from app.db.repositories.base import SQLAlchemyRepository
from app.db.models.user import User as UserModel
from app.models.domain.user import UserCreate


class UserRepository(SQLAlchemyRepository):
    sqla_model = UserModel

    create_schema = UserCreate
    # read_optional_schema = 
