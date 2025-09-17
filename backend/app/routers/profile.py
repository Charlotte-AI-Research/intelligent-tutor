from fastapi import APIRouter


router = APIRouter(prefix="/profile", tags=["profile"])


@router.get("/")
async def get_profile() -> dict:
    """Return a sample user profile."""
    return {"name": "Student One", "email": "student@example.com", "level": "beginner"}


