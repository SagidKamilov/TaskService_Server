import typing

from typing import List, Any

from src.schemas.users import UserSchemaAdd, UserSchemaDelete, UserSchemaEdit
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

    @staticmethod
    async def delete_users(uow: IUnitOfWork, user: UserSchemaDelete):
        users_dict = user.model_dump()
        async with uow:
            users = await uow.users.delete_one(**users_dict)
            await uow.commit()
            return users

    @staticmethod
    async def edit_user(uow: IUnitOfWork, user_id: int, user: UserSchemaEdit):
        users_dict: dict = user.model_dump()
        async with uow:
            user = await uow.users.edit_one(user_id, users_dict)
            await uow.commit()
            return user

    @staticmethod
    async def get_user(uow: IUnitOfWork, user_id: int):
        data: dict[str, Any] = {"id": user_id}
        async with uow:
            result = await uow.users.find_one(**data)
            return result

