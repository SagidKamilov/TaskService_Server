from src.models.users import Users
from src.repositories.abstract_repositories import SQLOrmRepository


class UserService(SQLOrmRepository):
    model = Users
