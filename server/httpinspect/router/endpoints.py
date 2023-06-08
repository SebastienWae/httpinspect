from uuid import UUID

from fastapi import APIRouter, Depends

from httpinspect.schemas.endpoint import EndpointSchema, EndpointSchemaCreate
from httpinspect.services.endpoint import EndpointService

router = APIRouter(prefix="/endpoints")


@router.get("/")
async def get_endpoints(
    owner_id: int,  # TODO: remove
    offset: int = 0,
    limit: int = 100,
    endpoint_service: EndpointService = Depends(EndpointService),
) -> list[EndpointSchema]:
    return await endpoint_service.get_enpoints_by_owner_id(
        owner_id,
        offset,
        limit,
    )


@router.post("/")
async def create_endpoit(
    endpoint_service: EndpointService = Depends(EndpointService),
) -> EndpointSchema | None:
    return await endpoint_service.create_endpoint(
        endpoint=EndpointSchemaCreate(name="test"),
        owner_id=1,
    )


@router.get("/{endpoint_id}")
async def get_endpoit(
    endpoint_id: UUID,
    endpoint_service: EndpointService = Depends(EndpointService),
) -> EndpointSchema | None:
    return await endpoint_service.get_endpoint(endpoint_id)


@router.delete("/{endpoint_id}")
async def delete_endpoint(
    endpoint_id: UUID,
    endpoint_service: EndpointService = Depends(EndpointService),
) -> None:
    await endpoint_service.remove_endpoint(endpoint_id)
