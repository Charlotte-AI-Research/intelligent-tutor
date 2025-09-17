"""Simple grading service placeholder."""

from typing import Tuple


def grade_answer(answer: str) -> Tuple[float, str]:
    """Return a mock score and feedback for an answer."""
    score = 0.8 if answer else 0.0
    feedback = "Good job!" if answer else "Please provide an answer."
    return score, feedback


