"""Domain model for a study session."""

from pydantic import BaseModel
from datetime import datetime


class StudySession(BaseModel):
    id: int
    title: str
    scheduled_for: datetime


