"""app/models/pydantic.py"""

from pydantic import BaseModel


class SummaryPayloadSchema(BaseModel):
    """summary payload schema"""
    url: str
