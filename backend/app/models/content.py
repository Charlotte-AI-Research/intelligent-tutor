"""Domain model for educational content items."""

from pydantic import BaseModel


class ContentItem(BaseModel):
    id: int
    title: str
    type: str  # e.g., video, article, course


