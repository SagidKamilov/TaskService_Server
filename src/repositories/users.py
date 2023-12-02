from src.models.users import Users
from src.repositories.abstract_repositories import SQLOrmRepository


class UserRepository(SQLOrmRepository):
    model = Users
