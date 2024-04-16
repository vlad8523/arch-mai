from typing import List

from sqlalchemy import select, ChunkedIteratorResult

from app.db.repositories.base import SQLAlchemyRepository
from app.db.models.user import User as UserModel
from app.models.domain.user import UserCreate, UserInDB


class UserRepository(SQLAlchemyRepository):
    sqla_model = UserModel

    create_schema = UserCreate
    # read_optional_schema = 


    async def get_user_by_email(self, email: str) -> List[UserInDB] | None:
        stmt = select(self.sqla_model).where(UserModel.email == email)

        res = await self.db.execute(stmt)    

        return res.fetchall()
        