from pydantic import BaseModel


class RequestSchemaBase(BaseModel):
    pass


class RequestSchemaCreate(RequestSchemaBase):
    pass


class RequestSchema(RequestSchemaBase):
    id: int  # noqa: A003
    endpoint_id: int

    class Config:
        orm_mode = True
