from src.models.tasks import TaskHistory
from src.repositories.abstract_repositories import SQLOrmRepository


class TasksHistoryRepository(SQLOrmRepository):
    model = TaskHistory
