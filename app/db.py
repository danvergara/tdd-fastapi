"""
app/db.py
"""

import logging
import os

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise

log = logging.getLogger(__name__)


def init_db(app: FastAPI) -> None:
    """
    Initialize the db
    """
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["app.models.tortoise"]},
        generate_schemas=False,
        add_exception_handlers=True,
    )


async def generate_schema() -> None:
    """Generte the db schema asynchronously"""
    log.info("initializing tortoise")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"), modules={"models": ["models.tortoise"]},
    )
    log.info("generating database schema via tortoise")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
