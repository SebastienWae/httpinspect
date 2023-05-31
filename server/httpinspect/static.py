from typing import Self

from fastapi import Response, status
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException
from starlette.types import Scope


class SPAStaticFiles(StaticFiles):
    async def get_response(self: Self, path: str, scope: Scope) -> Response:
        try:
            return await super().get_response(path, scope)
        except HTTPException as ex:
            if ex.status_code == status.HTTP_404_NOT_FOUND:
                return await super().get_response("index.html", scope)
            raise


static_app = SPAStaticFiles(directory="../client", html=True)
