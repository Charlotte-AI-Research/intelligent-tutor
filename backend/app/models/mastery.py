"""Domain model for tracking mastery levels of knowledge components."""

from pydantic import BaseModel


class Mastery(BaseModel):
    user_id: int
    kc_id: int
    level: float  # 0.0 - 1.0


