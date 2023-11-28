from src.models.tasks import Tasks
from src.repositories.abstract_repositories import SQLOrmRepository


class TasksRepository(SQLOrmRepository):
    model = Tasks
