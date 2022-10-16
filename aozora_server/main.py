from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from .routers import books

app = FastAPI(default_response_class=ORJSONResponse)


app.include_router(books.router)
