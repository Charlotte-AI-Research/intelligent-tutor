"""
Service: LLM interactions

This module will encapsulate calls to Large Language Models (LLMs) such as
OpenAI, local models, or other providers. For now, it returns canned responses
to keep the MVP simple and testable without credentials.
"""

from typing import Dict


def generate_tutor_reply(user_message: str) -> Dict[str, str]:
    """Return a simple canned response to simulate an LLM reply.

    Replace this with actual provider SDK calls (e.g., openai) later.
    """
    return {
        "reply": (
            "Thanks for sharing your goal! Let's break it down into steps. "
            "For now, try writing a short summary of what you want to learn."
        )
    }


