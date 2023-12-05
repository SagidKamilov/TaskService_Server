from fastapi import APIRouter

from src.schemas.users import UserSchemaAdd, UserSchemaDelete
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


@router.delete("")
async def delete_users(uow: UOWDep, user: UserSchemaDelete):
    result = await UserService().delete_users(uow, user)
    return {"deleted_row": result}
