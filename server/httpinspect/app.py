# from os import getenv

from fastapi import FastAPI

from httpinspect.database import init_db

# from httpinspect.models.endpoint import EndpointModel
# from httpinspect.models.user import UserModel
from httpinspect.router.auth import router as auth_router

# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
# from fastapi.middleware.trustedhost import TrustedHostMiddleware
# from starlette.middleware.sessions import SessionMiddleware
# from httpinspect.endpoint import endpoint_app
from httpinspect.router.endpoints import router as endpoint_router

# - [ ] alambic
# - [ ] router
# - [ ] auth middleware
# - [ ] openapi
# - [ ] tests


server = FastAPI()


@server.on_event("startup")
async def startup() -> None:
    await init_db()


# server.add_middleware(
#     TrustedHostMiddleware,
#     allowed_hosts=[getenv("APP_DOMAIN"), f"*.{getenv('APP_DOMAIN')}"],
# )

# server.add_middleware(
#     HTTPSRedirectMiddleware,
# )

# server.add_middleware(
#     SessionMiddleware,
#     secret_key=getenv("APP_SESSION_SECRET"),
#     https_only=True,
# )


server.include_router(endpoint_router, prefix="/api", tags=["endpoints"])
server.include_router(auth_router, prefix="/api", tags=["endpoints"])


# server.mount("/endpoint", endpoint_app)
