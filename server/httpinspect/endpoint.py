from collections.abc import Awaitable, Callable
from typing import Annotated

from fastapi import FastAPI, Path, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

endpoint_app = FastAPI()

endpoint_app.add_middleware(CORSMiddleware, allow_origins=["*"])


@endpoint_app.middleware("http")
async def session(
    request: Request,
    call_next: Callable[[Request], Awaitable[Response]],
) -> Response:
    response = await call_next(request)
    parts = request.url.path.split("/")
    if len(parts) != 3 and parts[2] != "123":
        return JSONResponse(content={"detail": "session id error"}, status_code=403)
    return response


@endpoint_app.get("/{session_id}")
async def get(session_id: Annotated[str, Path()]) -> str:
    return f"hello: {session_id}"


@endpoint_app.head("/{session_id}")
async def head(session_id: Annotated[str, Path()]) -> str:
    return f"hello: {session_id}"


@endpoint_app.post("/{session_id}")
async def post(session_id: Annotated[str, Path()]) -> str:
    return f"hello: {session_id}"


@endpoint_app.put("/{session_id}")
async def put(session_id: Annotated[str, Path()]) -> str:
    return f"hello: {session_id}"


@endpoint_app.delete("/{session_id}")
async def delete(session_id: Annotated[str, Path()]) -> str:
    return f"hello: {session_id}"


@endpoint_app.options("/{session_id}")
async def options(session_id: Annotated[str, Path()]) -> str:
    return f"hello: {session_id}"


@endpoint_app.trace("/{session_id}")
async def trace(session_id: Annotated[str, Path()]) -> str:
    return f"hello: {session_id}"


@endpoint_app.patch("/{session_id}")
async def patch(session_id: Annotated[str, Path()]) -> str:
    return f"hello: {session_id}"
