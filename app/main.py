"""app/main.py"""
import logging

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    """Returns an instance of FastAPI with all the settings"""
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router,
        prefix="/summaries",
        tags=["summaries"],
    )

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    """initialize the db on startup"""
    log.info("starting up")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    """shutdown"""
    log.info("shutting down")
