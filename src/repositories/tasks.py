from src.models.tasks import Tasks
from src.repositories.sql_repositories import SQLOrmRepository


class TasksRepository(SQLOrmRepository):
    model = Tasks
