"""
app/api/ping.py
"""

from fastapi import APIRouter, Depends

from app.config import get_settings, Settings

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """
    /ping endpoint
    """
    return {
        "ping": "pong",
        "environment": settings.environment,
        "testing": settings.testing,
    }
