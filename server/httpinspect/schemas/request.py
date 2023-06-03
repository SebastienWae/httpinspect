from typing import Any, Literal

from pydantic import BaseModel, Json
from starlette.datastructures import URL, FormData, Headers, QueryParams


class Request(BaseModel):
    uid: int
    method: Literal["GET", "POST"]
    url: URL
    headers: Headers
    query: QueryParams
    body: bytes | FormData | Json[Any]
