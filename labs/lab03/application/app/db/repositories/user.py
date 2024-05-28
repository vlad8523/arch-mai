from typing import List

from sqlalchemy import select, update

from app.db.repositories.base import SQLAlchemyRepository
from app.db.models.user import User as UserModel
from app.models.domain.user import  UserData, UserCreate, UserInDB
from app.core.security import get_password_hash

class UserRepository(SQLAlchemyRepository):
    sqla_model = UserModel

    create_schema = UserCreate
    # read_optional_schema = 

    async def create(
        self, 
        obj_new: create_schema
    ) -> sqla_model | None:
        try:
            data = obj_new.model_dump()

            data.update(
                hashed_password = get_password_hash(obj_new.password)
            )

            del data["password"]

            print(data)
            db_obj_new = self.sqla_model(**data)

            self.db.add(db_obj_new)

            await self.db.commit()
            await self.db.refresh(db_obj_new)

            print(db_obj_new)

            return db_obj_new
        
        except Exception as e:
            print(f"error: {e}")
            await self.db.rollback()
            return None

    async def get_user_by_email(self, email: str) -> UserInDB | None:
        stmt = select(self.sqla_model).where(UserModel.email==email)

        res = await self.db.execute(stmt)    

        return res.scalar_one_or_none()
    

    async def get_user_by_username(self, username: str) -> UserModel| None:
        stmt = select(self.sqla_model).where(UserModel.username==username)

        res = await self.db.execute(stmt)    

        return res.scalar_one_or_none()
    

    async def get_users_by_first_and_second_name(self, first_name: str, second_name: str) -> List[UserInDB] | None:
        stmt = select(self.sqla_model).where(UserModel.first_name==first_name).where(UserModel.second_name==second_name)

        res = await self.db.execute(stmt)

        return res.fetchall()
        

    async def update_user(self, user_id: int, user_update: UserData):
        data = user_update.model_dump()

        data.update(
            hashed_password = get_password_hash(data["password"])
        )

        del data["password"]

        stmt = update(self.sqla_model).where(UserModel.id==user_id).values(data)

        print(stmt)

        await self.db.execute(stmt)

        await self.db.commit()