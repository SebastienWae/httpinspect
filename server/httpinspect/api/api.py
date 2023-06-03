from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

api_app = FastAPI()

api_app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["example.com", "*.example.com"],  # TODO
)

api_app.add_middleware(
    HTTPSRedirectMiddleware,
)

api_app.add_middleware(
    SessionMiddleware,
    secret_key="123",  # TODO
    https_only=True,
)
