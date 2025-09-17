"""Content recommendation service placeholder."""

from typing import List, Dict


def recommend_content(goal_text: str) -> List[Dict[str, str]]:
    """Return a small list of recommended content based on the goal text."""
    base = [
        {"id": "intro-python", "title": "Intro to Python", "type": "video"},
        {"id": "data-structures", "title": "Data Structures 101", "type": "article"},
    ]
    if "algorithm" in goal_text.lower():
        base.append({"id": "algorithms", "title": "Algorithms Crash Course", "type": "course"})
    return base


