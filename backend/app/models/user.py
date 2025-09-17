"""
Pydantic models related to users. These are used to validate request/response
payloads for API endpoints. They are not ORM models.
"""

from typing import List, Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    """Represents a user in API responses/requests."""

    id: int
    name: str
    email: Optional[EmailStr] = None
    goals: List[str] = []


