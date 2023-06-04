from os import getenv

from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

from httpinspect.database import Base
from httpinspect.endpoint import endpoint_app

from .database import engine

# - [ ] alambic
# - [ ] router
# - [ ] auth middleware
# - [ ] openapi
# - [ ] tests

Base.metadata.create_all(bind=engine)


app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[getenv("APP_DOMAIN"), f"*.{getenv('APP_DOMAIN')}"],
)

app.add_middleware(
    HTTPSRedirectMiddleware,
)

app.add_middleware(
    SessionMiddleware,
    secret_key=getenv("APP_SESSION_KEY"),
    https_only=True,
)


app.mount("/endpoint", endpoint_app)
