from logging import getLogger

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from cats.api import breeds, cats, index
from cats.ioc import init_async_container

logger = getLogger(__name__)


def create_app() -> FastAPI:
    container = init_async_container()
    app = FastAPI()
    app.include_router(cats.router)
    app.include_router(breeds.router)
    app.include_router(index.router)
    setup_dishka(container, app)

    logger.info("App created")
    return app
