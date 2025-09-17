"""Study session scheduler placeholder."""

from datetime import datetime, timedelta
from typing import List, Dict


def schedule_study_sessions(days: int = 7) -> List[Dict[str, str]]:
    """Return mock scheduled sessions for the next `days` days."""
    start = datetime.now()
    sessions: List[Dict[str, str]] = []
    for i in range(1, days + 1):
        when = start + timedelta(days=i)
        sessions.append({"title": f"Session {i}", "datetime": when.isoformat(timespec="minutes")})
    return sessions


