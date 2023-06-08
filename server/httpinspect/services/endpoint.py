from typing import Self
from uuid import UUID, uuid4

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from httpinspect.database import get_db
from httpinspect.models.endpoint import EndpointModel
from httpinspect.schemas.endpoint import EndpointSchema, EndpointSchemaCreate


class EndpointService:
    def __init__(self: Self, db: AsyncSession = Depends(get_db)) -> None:
        self._db = db

    async def get_endpoint(
        self: Self,
        endpoint_id: UUID,
    ) -> EndpointSchema | None:
        endpoint = await self._db.get(EndpointModel, endpoint_id)
        if endpoint is None:
            return None
        return EndpointSchema.from_orm(endpoint)

    async def get_enpoints_by_owner_id(
        self: Self,
        owner_id: int,
        offset: int = 0,
        limit: int = 100,
    ) -> list[EndpointSchema]:
        transaction = await self._db.scalars(
            select(EndpointModel)
            .filter_by(owner_id=owner_id)
            .offset(offset)
            .limit(limit),
        )
        return [
            EndpointSchema.from_orm(endpoint) for endpoint in transaction.all()
        ]

    async def search_endpoint_with_name(
        self: Self,
        endpoint_name: str,
        offset: int = 0,
        limit: int = 100,
    ) -> list[EndpointSchema]:
        transaction = await self._db.scalars(
            select(EndpointModel)
            .filter(
                EndpointModel.name.match(endpoint_name),
            )
            .offset(offset)
            .limit(limit),
        )
        return [
            EndpointSchema.from_orm(endpoint) for endpoint in transaction.all()
        ]

    async def get_endpoints(
        self: Self,
        offset: int = 0,
        limit: int = 100,
    ) -> list[EndpointSchema]:
        transaction = await self._db.scalars(
            select(EndpointModel).offset(offset).limit(limit),
        )
        return [
            EndpointSchema.from_orm(endpoint) for endpoint in transaction.all()
        ]

    async def create_endpoint(
        self: Self,
        endpoint: EndpointSchemaCreate,
        owner_id: int,
    ) -> EndpointSchema:
        db_endpoint = EndpointModel(
            **endpoint.dict(),
            id=uuid4(),
            owner_id=owner_id,
        )
        self._db.add(db_endpoint)
        await self._db.commit()
        await self._db.refresh(db_endpoint)
        return EndpointSchema.from_orm(db_endpoint)

    async def remove_endpoint(self: Self, endpoint_id: UUID) -> bool:
        endpoint = await self._db.get(EndpointModel, endpoint_id)
        if endpoint is None:
            return False
        await self._db.delete(endpoint)
        await self._db.commit()
        return True
