"""
app/api/summaries.py
"""

from typing import List

from fastapi import APIRouter, HTTPException, Path

from app.api import crud
from app.models.pydantic import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummaryUpdatePayloadSchema,
)
from app.models.tortoise import SummarySchema

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


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int = Path(..., gt=0)) -> SummarySchema:
    """
    Returns a summary from db
    """
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="summary not found")

    return summary


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    """
    Returns all summaries in db
    """
    return await crud.get_all()


@router.delete("/{id}/", response_model=SummaryResponseSchema)
async def delete_summary(id: int = Path(..., gt=0)) -> SummaryResponseSchema:
    """deletes a summary from db"""
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="summary not found")

    await crud.delete(id)

    return summary


@router.put("/{id}/", response_model=SummarySchema)
async def update_summary(
    payload: SummaryUpdatePayloadSchema, id: int = Path(..., gt=0)
) -> SummarySchema:
    """updates an existingsummary in db"""
    summary = await crud.put(id, payload)
    if not summary:
        raise HTTPException(status_code=404, detail="summary not found")

    return summary
