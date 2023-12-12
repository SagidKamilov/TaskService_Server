from fastapi import APIRouter

from src.schemas.users import UserSchemaAdd, UserSchemaEdit
from src.services.users import UserService

from src.api.dependencies import UOWDep

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(user: UserSchemaAdd, uow: UOWDep):
    user_id = await UserService().add_user(uow, user)
    return user_id


@router.get("")
async def get_users(uow: UOWDep):
    users = await UserService().get_users(uow)
    return users


@router.delete("/{user_id}")
async def delete_user(uow: UOWDep, user_id: int):
    result = await UserService().delete_user(uow, user_id)
    return {"deleted_row": result}


@router.patch("/{user_id}")
async def edit_users(uow: UOWDep, user_id: int, user: UserSchemaEdit):
    result = await UserService().edit_user(uow, user_id, user)
    return {"user_id": result}


@router.get("/{user_id}")
async def get_user(uow: UOWDep, user_id: int):
    user = await UserService().get_user(uow, user_id)
    return user
