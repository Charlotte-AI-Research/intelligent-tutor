"""Domain model for knowledge components (skills/concepts)."""

from pydantic import BaseModel


class KnowledgeComponent(BaseModel):
    id: int
    name: str
    description: str


