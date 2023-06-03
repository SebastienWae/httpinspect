from fastapi import FastAPI

from httpinspect.api.api import api_app
from httpinspect.endpoint import endpoint_app
from httpinspect.static import static_app

app = FastAPI()
app.mount("/api", api_app)
app.mount("/endpoint", endpoint_app)
app.mount("/", static_app)
