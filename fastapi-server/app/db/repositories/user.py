from typing import List

from sqlalchemy import select

from app.db.repositories.base import SQLAlchemyRepository
from app.db.models.user import User as UserModel
from app.models.domain.user import UserCreate, UserInDB


class UserRepository(SQLAlchemyRepository):
    sqla_model = UserModel

    create_schema = UserCreate
    # read_optional_schema = 


    async def get_users_by_email(self, email: str) -> List[UserInDB] | None:
        stmt = select(self.sqla_model).where(UserModel.email==email)

        res = await self.db.execute(stmt)    

        return res.fetchall()
    

    async def get_users_by_first_and_second_name(self, first_name: str, second_name: str) -> List[UserInDB] | None:
        stmt = select(self.sqla_model).where(UserModel.first_name==first_name).where(UserModel.second_name==second_name)

        res = await self.db.execute(stmt)

        return res.fetchall()
        