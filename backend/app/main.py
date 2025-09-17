from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Router imports (each router groups related endpoints)
try:
    from .routers import goals, roadmap, content, assessments, profile, calendar
except Exception:

    goals = roadmap = content = assessments = profile = calendar = None


def create_app() -> FastAPI:
    """
    Factory function to create and configure the FastAPI application.

    Keeping app creation in a function makes it easier to test and extend.
    """
    app = FastAPI(title="Intelligent Tutor API", version="0.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    if goals is not None:
        app.include_router(goals.router)
    if roadmap is not None:
        app.include_router(roadmap.router)
    if content is not None:
        app.include_router(content.router)
    if assessments is not None:
        app.include_router(assessments.router)
    if profile is not None:
        app.include_router(profile.router)
    if calendar is not None:
        app.include_router(calendar.router)

    @app.get("/health")
    async def health_check() -> dict:
        """Simple health check endpoint for uptime monitoring."""
        return {"status": "ok"}

    return app


app = create_app()


