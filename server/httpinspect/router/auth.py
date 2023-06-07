from fastapi import APIRouter, Depends

from httpinspect.schemas.user import UserSchema, UserSchemaCreate
from httpinspect.services.user import UserService

router = APIRouter(prefix="/auth")


@router.post("/signup")
async def signup(
    user_service: UserService = Depends(UserService),
) -> UserSchema | None:
    return await user_service.create_user(user=UserSchemaCreate(email="test"))


@router.get("/")
async def get_users(
    user_service: UserService = Depends(UserService),
) -> list[UserSchema]:
    return await user_service.get_users()
