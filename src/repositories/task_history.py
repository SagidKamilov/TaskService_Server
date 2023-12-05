from src.models.tasks import TaskHistory
from src.repositories.sql_repositories import SQLOrmRepository


class TasksHistoryRepository(SQLOrmRepository):
    model = TaskHistory
