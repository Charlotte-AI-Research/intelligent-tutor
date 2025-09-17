from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


router = APIRouter(prefix="/goals", tags=["goals"])


class GoalCreate(BaseModel):
    """Payload for creating a new learning goal."""
    text: str


@router.get("/")
async def list_goals() -> dict:
    """Return a small sample list of goals.

    In a real implementation, this would read from a database.
    """
    sample: List[str] = [
        "Learn Python basics",
        "Master data structures",
        "Prepare for algorithms interview",
    ]
    return {"goals": sample}


@router.post("/")
async def create_goal(payload: GoalCreate) -> dict:
    """Echo back the goal text for now.

    Replace this with DB insertion and scheduling logic later on.
    """
    return {"message": "Goal received", "goal": payload.text}


