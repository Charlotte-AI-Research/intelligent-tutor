from fastapi import APIRouter


router = APIRouter(prefix="/content", tags=["content"])


@router.get("/")
async def list_content() -> dict:
    """Return a small set of example content cards."""
    return {
        "items": [
            {"id": 1, "title": "Intro to Python", "type": "video"},
            {"id": 2, "title": "Data Structures Notes", "type": "article"},
        ]
    }


