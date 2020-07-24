"""
app/api/crud.py
"""
from typing import Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """
    post creates a new summary in db, given a valid payload
    """
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    """
    Returns a Summary from database
    """
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
