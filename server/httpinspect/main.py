from fastapi import FastAPI

from .static import static_app

app = FastAPI()
app.mount("/", static_app)
