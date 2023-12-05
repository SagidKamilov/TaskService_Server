from typing import List

from src.repositories.abstract_repositories import AbstractRepository
from src.schemas.users import UserSchemaAdd, UserSchemaGet
from src.utils.unitofwork import IUnitOfWork


class UserService:
    @staticmethod
    async def add_user(uow: IUnitOfWork, user: UserSchemaAdd):
        users_dict = user.model_dump()
        async with uow:
            user_id = await uow.users.add_one(users_dict)
            await uow.commit()
            return user_id

    @staticmethod
    async def get_users(uow: IUnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users
