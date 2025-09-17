"""Seed script for development.

Currently a placeholder that ensures the DB can initialize.
Run with: `python scripts/seed_db.py` from the project root.
"""

from backend.app.db.database import init_db


def main() -> None:
    init_db()
    print("Database initialized (placeholder).")


if __name__ == "__main__":
    main()


