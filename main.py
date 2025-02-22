import logging
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from routers.urls import URLS
from fastapi_dynamic_routers import Routers

from contextlib import asynccontextmanager
from alembic.config import Config
from alembic import command

def run_migrations():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

@asynccontextmanager
async def lifespan(app_: FastAPI):
    # log.info("Starting up...")
    # log.info("run alembic upgrade head...")
    run_migrations()
    yield
    # log.info("Shutting down...")


app = FastAPI(lifespan=lifespan)

app.title = "myStock api"
app.version = "0.0.1"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/api/login" )
routers = Routers(app, URLS, '/v1/api')()

# log = logging.getLogger("uvicorn")



