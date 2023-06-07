from typing import Self

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from httpinspect.database import get_db
from httpinspect.models.user import UserModel
from httpinspect.schemas.user import UserSchema, UserSchemaCreate


class UserService:
    def __init__(self: Self, db: AsyncSession = Depends(get_db)) -> None:
        self._db = db

    async def get_user(self: Self, user_id: int) -> UserModel | None:
        return await self._db.get(UserModel, user_id)

    async def get_user_by_email(
        self: Self,
        email: str,
    ) -> UserSchema | None:
        transaction = await self._db.scalars(
            select(UserModel).filter_by(email=email).limit(1),
        )
        user = transaction.first()
        if user is None:
            return None
        return UserSchema.from_orm(user)

    async def get_users(
        self: Self,
        skip: int = 0,
        limit: int = 100,
    ) -> list[UserSchema]:
        transaction = await self._db.scalars(
            select(UserModel).offset(skip).limit(limit),
        )
        return [UserSchema.from_orm(endpoint) for endpoint in transaction.all()]

    async def create_user(
        self: Self,
        user: UserSchemaCreate,
    ) -> UserSchema:
        db_user = UserModel(**user.dict())
        self._db.add(db_user)
        await self._db.commit()
        await self._db.refresh(db_user)
        return UserSchema.from_orm(db_user)
