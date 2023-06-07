from uuid import UUID

from pydantic import BaseModel


class EndpointSchemaBase(BaseModel):
    name: str


class EndpointSchemaCreate(EndpointSchemaBase):
    pass


class EndpointSchema(EndpointSchemaBase):
    id: UUID  # noqa: A003
    owner_id: int

    class Config:
        orm_mode = True
