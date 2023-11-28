from typing import List

from src.repositories.abstract_repositories import AbstractRepository
from src.schemas.tasks import TaskSchemaAdd


class TasksService:
    def __init__(self, tasks_repo: AbstractRepository):
        self.tasks_repo: AbstractRepository = tasks_repo

    async def add_task(self, task: TaskSchemaAdd) -> int:
        tasks_dict = task.model_dump()
        task_id: int = await self.tasks_repo.add_one(data=tasks_dict)
        return task_id

    async def get_tasks(self) -> List[int]:
        tasks = await self.tasks_repo.find_all()
        return tasks
