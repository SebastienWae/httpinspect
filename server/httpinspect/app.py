from fastapi import FastAPI

from httpinspect.endpoint import endpoint_app
from httpinspect.router.auth import router as auth_router
from httpinspect.router.endpoints import router as endpoint_router
from httpinspect.router.requests import router as request_router

# - [x] alambic
# - [x] authorization
# - [ ] error handling
# - [ ] router
# - [ ] auth middleware
# - [ ] tests


server = FastAPI()


server.include_router(auth_router, prefix="/api", tags=["auth"])
server.include_router(endpoint_router, prefix="/api", tags=["endpoints"])
server.include_router(request_router, prefix="/api", tags=["requests"])


server.mount("/endpoint", endpoint_app)
