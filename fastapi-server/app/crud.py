# from typing import Any

# from sqlmodel import Session, select

# from models.user import User, UserCreate, UserSearchFirstSecondName, UserUpdateMe
# from core.security import get_password_hash, verify_password


# def create_user(*, session: Session, user_create: UserCreate) -> User:
#     db_obj = User.model_validate(
#         user_create, update={"hashed_password": get_password_hash(user_create.password)}
#     )
#     session.add(db_obj)
#     session.commit()
#     session.refresh(db_obj)
#     return db_obj

        
# def get_user_by_email(*, session: Session, email: str) -> User | None:
#     statement = select(User).where(User.email == email)
#     session_user = session.exec(statement).first()
#     return session_user


# def get_user_by_id(*, session: Session, id: int) -> User | None:
#     statement = select(User).where(User.id == id)
#     session_user = session.exec(statement).first()
#     return session_user


# def search_user(*, session: Session, 
#                 user_search: UserSearchFirstSecondName):
#     statement = select(User).where(User.first_name == user_search.first_name).where(User.second_name == user_search.second_name)
#     session_users = session.exec(statement).all()
#     return session_users


# def update_user(*, session: Session,
#                 db_user: User,
#                 user_in: UserUpdateMe):
#     user_data = user_in.model_dump(exclude_unset=True)
#     db_user.sqlmodel_update(user_data)
#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     return db_user


# def authentificate(*, session: Session, email: str, password: str) -> User | None:
#     db_user = get_user_by_email(session=session, email=email)
#     if not db_user:
#         return None
#     if not verify_password(password, db_user.hashed_password):
#         return None
#     return db_user