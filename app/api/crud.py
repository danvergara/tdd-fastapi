"""
app/api/crud.py
"""
from typing import Union, List

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary
from app.summarizer import generate_summary


async def post(payload: SummaryPayloadSchema) -> int:
    """
    post creates a new summary in db, given a valid payload
    """
    article_summary = generate_summary(payload.url)
    summary = TextSummary(url=payload.url, summary=article_summary)
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    """
    Returns a Summary from database
    """
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]


async def get_all() -> List:
    """
    Returns all summaries in db
    """
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    """Deletes a summary in db"""
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Union[dict, None]:
    """updates an existing summary in db"""
    summary = await TextSummary.filter(id=id).update(
        url=payload.url, summary=payload.summary,
    )
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary[0]
