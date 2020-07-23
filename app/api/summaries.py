"""
app/api/summaries.py
"""

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    """
    Create a summary in db
    """
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url,
    }

    return response_object
