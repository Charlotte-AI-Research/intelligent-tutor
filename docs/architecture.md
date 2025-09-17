## Architecture Overview

Intelligent Tutor is a simple two-tier application:

- Backend: FastAPI (Python) providing REST endpoints for goals, content, roadmap, assessments, profile, and calendar.
- Frontend: React (Vite) single-page app that consumes the backend API.

### Backend
- `app/main.py`: FastAPI app factory, CORS, and router registration. Includes `/health`.
- `app/routers/*`: Feature-specific endpoints grouped by domain.
- `app/services/*`: Business logic (LLM calls, grading, recommendations, scheduling). Currently mocked.
- `app/models/*`: Pydantic models for request/response validation.
- `app/db/database.py`: SQLAlchemy session setup (SQLite for local dev).
- `tests/`: Basic unit tests with `pytest`.

### Frontend
- `src/pages/*`: Top-level pages like landing (`index.jsx`), `dashboard.jsx`, `sessions.jsx`, `profile.jsx`.
- `src/components/*`: Reusable UI building blocks.
- `src/utils/api.js`: API helper functions for calling the backend.
- `public/`: Static assets.

### Dev Flow
1. Start backend: `uvicorn app.main:app --reload` from `backend/`.
2. Start frontend: `npm run dev` from `frontend/`.
3. Visit the SPA at `http://localhost:5173`. Backend runs on `http://localhost:8000`.


