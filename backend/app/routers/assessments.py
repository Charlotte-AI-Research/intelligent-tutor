from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/assessments", tags=["assessments"])


class Submission(BaseModel):
    question_id: int
    answer: str


@router.post("/grade")
async def grade_submission(payload: Submission) -> dict:
    """Mock grading endpoint that returns a fixed score."""
    return {"question_id": payload.question_id, "score": 0.8, "feedback": "Good job!"}


