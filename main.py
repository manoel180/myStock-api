import logging
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from routers.urls import URLS
from fastapi_dynamic_routers import Routers

from contextlib import asynccontextmanager
from alembic.config import Config
from alembic import command
from fastapi.middleware.cors import CORSMiddleware

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
    

@asynccontextmanager
async def lifespan(app_: FastAPI):
    log.info("Starting up...")
    log.info("run alembic upgrade head...")
    run_migrations()
    yield
    log.info("Shutting down...")


app = FastAPI(lifespan=lifespan)
app.debug=True

app.title = "myStock api"
app.version = "0.0.1"

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/api/login" )
routers = Routers(app, URLS, '/v1/api')()

log = logging.getLogger("uvicorn")



