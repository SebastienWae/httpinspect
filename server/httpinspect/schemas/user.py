from pydantic import BaseModel


class UserSchemaBase(BaseModel):
    email: str


class UserSchemaCreate(UserSchemaBase):
    pass


class UserSchema(UserSchemaBase):
    id: int  # noqa: A003

    class Config:
        orm_mode = True
