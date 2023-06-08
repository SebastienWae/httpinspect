from uuid import UUID

from fastapi import APIRouter, Depends

from httpinspect.schemas.request import RequestSchema
from httpinspect.services.request import RequestService

router = APIRouter(prefix="/requests")


@router.get("/")
async def get_requests(
    endpoint_id: UUID,
    offset: int = 0,
    limit: int = 100,
    request_service: RequestService = Depends(RequestService),
) -> list[RequestSchema]:
    return await request_service.get_requests_by_endpoint_id(
        endpoint_id,
        offset,
        limit,
    )


@router.get("/{request_id}")
async def get_request(
    request_id: int,
    request_service: RequestService = Depends(RequestService),
) -> RequestSchema | None:
    return await request_service.get_request(request_id)


@router.delete("/{request_id}")
async def delete_request(
    request_id: int,
    request_service: RequestService = Depends(RequestService),
) -> None:
    await request_service.remove_request(request_id)
