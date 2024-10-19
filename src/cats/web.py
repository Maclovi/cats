from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from logging import getLogger

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from cats.api import breeds, cats, index
from cats.ioc import init_async_container

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield None
    await app.state.dishka_container.close()


def create_app() -> FastAPI:
    container = init_async_container()
    app = FastAPI(lifespan=lifespan)
    app.include_router(cats.router)
    app.include_router(breeds.router)
    app.include_router(index.router)
    setup_dishka(container, app)

    logger.info("App created")
    return app
