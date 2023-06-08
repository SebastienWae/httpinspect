from typing import Self
from uuid import UUID

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from httpinspect.database import get_db
from httpinspect.models.request import RequestModel
from httpinspect.schemas.request import RequestSchema, RequestSchemaCreate


class RequestService:
    def __init__(self: Self, db: AsyncSession = Depends(get_db)) -> None:
        self._db = db

    async def get_request(
        self: Self,
        request_id: int,
    ) -> RequestSchema | None:
        request = await self._db.get(RequestModel, request_id)
        if request is None:
            return None
        return RequestSchema.from_orm(request)

    async def get_requests_by_endpoint_id(
        self: Self,
        endpoint_id: UUID,
        offset: int = 0,
        limit: int = 100,
    ) -> list[RequestSchema]:
        transaction = await self._db.scalars(
            select(RequestModel)
            .filter_by(endpoint_id=endpoint_id)
            .offset(offset)
            .limit(limit),
        )
        return [
            RequestSchema.from_orm(endpoint) for endpoint in transaction.all()
        ]

    async def create_request(
        self: Self,
        request: RequestSchemaCreate,
        endpoint_id: UUID,
    ) -> RequestSchema:
        db_request = RequestModel(
            **request.dict(),
            endpoint_id=endpoint_id,
        )
        self._db.add(db_request)
        await self._db.commit()
        await self._db.refresh(db_request)
        return RequestSchema.from_orm(db_request)

    async def remove_request(self: Self, request_id: int) -> bool:
        request = await self._db.get(RequestModel, request_id)
        if request is None:
            return False
        await self._db.delete(request)
        await self._db.commit()
        return True
