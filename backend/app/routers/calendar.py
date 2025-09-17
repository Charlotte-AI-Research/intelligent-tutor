from fastapi import APIRouter
from datetime import date, timedelta


router = APIRouter(prefix="/calendar", tags=["calendar"])


@router.get("/upcoming")
async def upcoming_events() -> dict:
    """Return sample upcoming study sessions."""
    today = date.today()
    return {
        "events": [
            {"title": "Study Python", "date": str(today + timedelta(days=1))},
            {"title": "Data Structures Practice", "date": str(today + timedelta(days=3))},
        ]
    }


