from uuid import UUID

from fastapi import APIRouter, Depends

from httpinspect.schemas.endpoint import EndpointSchema, EndpointSchemaCreate
from httpinspect.services.endpoint import EndpointService

router = APIRouter(prefix="/endpoints")


@router.get("/{endpoint_id}")
async def get_endpoit(
    endpoint_id: UUID,
    endpoint_service: EndpointService = Depends(EndpointService),
) -> EndpointSchema | None:
    return await endpoint_service.get_endpoint(endpoint_id)


@router.post("/")
async def create_endpoit(
    endpoint_service: EndpointService = Depends(EndpointService),
) -> EndpointSchema | None:
    return await endpoint_service.create_endpoint(
        endpoint=EndpointSchemaCreate(name="test"),
        owner_id=1,
    )
