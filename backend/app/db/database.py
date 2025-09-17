"""
Database configuration.

For the MVP we use a local SQLite database via SQLAlchemy. This file sets up
an engine and a session factory. Real projects may also configure Alembic
migrations and environment-based settings.
"""

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# SQLite database file stored in project root for simplicity
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"


# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    """Yield a database session to routes/services and ensure it closes."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Placeholder for initializing the database (migrations, seed data, etc.).

    For now, this function simply verifies we can connect to the database by
    opening and closing a session.
    """
    db = SessionLocal()
    db.close()


