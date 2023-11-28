from typing import List

from src.repositories.abstract_repositories import AbstractRepository
from src.schemas.users import UserSchemaAdd


class UserService:
    def __init__(self, users_repo: AbstractRepository):
        self.user_repo: AbstractRepository = users_repo

    async def add_user(self, user: UserSchemaAdd) -> int:
        users_dict = user.model_dump()
        user_id: int = await self.user_repo.add_one(data=users_dict)
        return user_id

    async def get_users(self) -> List[int]:
        users = await self.user_repo.find_all()
        return users
