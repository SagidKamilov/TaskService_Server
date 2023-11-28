from typing import Annotated, Dict, List

from fastapi import APIRouter, Depends

from src.schemas.users import UserSchemaAdd
from src.services.users import UserService

from dependencies import users_service

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("")
async def add_user(user: UserSchemaAdd, user_add_service: Annotated[UserService, Depends(users_service)]) -> Dict[str, int]:
    user_id = await user_add_service.add_user(user)
    return {"user_id": user_id}


@router.get("")
async def get_users(user_service: Annotated[UserService, Depends(users_service)]) -> List[int]:
    users = await user_service.get_users()
    return users
