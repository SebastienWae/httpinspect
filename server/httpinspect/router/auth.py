from fastapi import APIRouter, Depends

from httpinspect.schemas.user import UserSchema, UserSchemaCreate
from httpinspect.services.user import UserService

router = APIRouter(prefix="/auth")


@router.get("/me")
@router.patch("/me")
@router.delete("/me")
@router.post("/login")
@router.post("/logout")
@router.post("/register")
async def signup(
    user_service: UserService = Depends(UserService),
) -> UserSchema | None:
    return await user_service.create_user(user=UserSchemaCreate(email="test"))
