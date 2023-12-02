from typing import Annotated, Dict, List

from fastapi import APIRouter, Depends

from src.schemas.tasks import TaskSchemaAdd, TaskSchemaGet
from src.services.tasks import TasksService

from src.api.dependencies import tasks_service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("")
async def add_task(task: TaskSchemaAdd, task_add_service: Annotated[TasksService, Depends(tasks_service)]) -> Dict[str, int]:
    task_id = await task_add_service.add_task(task)
    return {"task_id": task_id}


@router.get("")
async def get_tasks(task_service: Annotated[TasksService, Depends(tasks_service)]) -> List[TaskSchemaGet]:
    tasks = await task_service.get_tasks()
    return tasks

