"""app/models/pydantic.py"""

from pydantic import BaseModel, AnyHttpUrl


class SummaryPayloadSchema(BaseModel):
    """summary payload schema"""

    url: AnyHttpUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    """
    SummaryResponseSchema is the actual response of the summaries endpoints.
    Inherits from the SummaryPayloadSchema model, adding an id field.
    """

    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    """SummaryUpdatePayloadSchema"""

    summary: str
