from fastapi import APIRouter

from src.schemas.users import UserSchemaAdd
from src.services.users import UserService

from src.api.dependencies import UOWDep

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(user: UserSchemaAdd, uow: UOWDep):
    user_id = await UserService().add_user(uow, user)
    return {"user_id": user_id}


@router.get("")
async def get_users(uow: UOWDep):
    users = await UserService().get_users(uow)
    return users
