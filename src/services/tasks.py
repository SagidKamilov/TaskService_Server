from src.schemas.tasks import TaskSchemaAdd, TaskSchemaEdit, TaskHistorySchemaAdd, TaskDeleteSchema
from src.utils.unitofwork import IUnitOfWork, UnitOfWork


class TasksService:
    @staticmethod
    async def add_task(uow: IUnitOfWork, task: TaskSchemaAdd):
        tasks_dict: dict = task.model_dump()
        async with uow:
            task_id = await uow.tasks.add_one(tasks_dict)
            await uow.commit()
            return task_id

    @staticmethod
    async def get_tasks(uow: IUnitOfWork):
        async with uow:
            tasks = await uow.tasks.find_all()
            return tasks

    @staticmethod
    async def edit_task(uow: IUnitOfWork, task_id: int, task: TaskSchemaEdit):
        tasks_dict: dict = task.model_dump()
        async with uow:
            await uow.tasks.edit_one(task_id, tasks_dict)

            cur_task = await uow.tasks.find_one(id=task_id)
            task_history_log = TaskHistorySchemaAdd(
                task_id=task_id,
                previous_assignee_id=cur_task.assignee_id,
                new_assignee_id=task.assignee_id
            )
            task_history_log = task_history_log.model_dump()
            await uow.task_history.add_one(task_history_log)
            await uow.commit()

    @staticmethod
    async def get_task_history(uow: IUnitOfWork):
        async with uow:
            history = await uow.task_history.find_all()
            return history

    @staticmethod
    async def delete_task(uow: UnitOfWork, task: TaskDeleteSchema):
        task_dict: dict = task.model_dump()
        async with uow:
            check = await uow.tasks.delete_one(task_dict)
            await uow.commit()
            return check
