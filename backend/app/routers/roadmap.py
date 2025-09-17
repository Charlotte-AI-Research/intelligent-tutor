from fastapi import APIRouter


router = APIRouter(prefix="/roadmap", tags=["roadmap"])


@router.get("/")
async def get_sample_roadmap() -> dict:
    """Return a simple static learning roadmap."""
    return {
        "steps": [
            {"title": "Basics", "items": ["Variables", "Control Flow", "Functions"]},
            {"title": "Intermediate", "items": ["Data Structures", "OOP"]},
            {"title": "Advanced", "items": ["Algorithms", "Projects"]},
        ]
    }


