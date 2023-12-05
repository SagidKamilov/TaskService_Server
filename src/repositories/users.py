from src.models.users import Users
from src.repositories.sql_repositories import SQLOrmRepository


class UsersRepository(SQLOrmRepository):
    model = Users
