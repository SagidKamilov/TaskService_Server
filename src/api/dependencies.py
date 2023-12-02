from src.repositories.tasks import TasksRepository
from src.repositories.users import UserRepository
from src.services.tasks import TasksService
from src.services.users import UserService


def tasks_service() -> TasksService:
    return TasksService(tasks_repo=TasksRepository)


def users_service() -> UserService:
    return UserService(users_repo=UserRepository)
