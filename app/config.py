"""app/config"""
import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    """Settings"""

    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.getenv("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    """get settings"""
    log.info("loading config settings from the environment")
    return Settings()
