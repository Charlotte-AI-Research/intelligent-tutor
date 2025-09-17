#!/usr/bin/env bash

# Start backend (FastAPI) and frontend (Vite) together for development.
# Usage: bash scripts/run_dev.sh

set -euo pipefail

# Start backend
(
  cd backend
  echo "Starting backend at http://localhost:8000 ..."
  uvicorn app.main:app --reload
) &

BACKEND_PID=$!

# Start frontend
(
  cd frontend
  echo "Starting frontend at http://localhost:5173 ..."
  npm run dev --silent
) &

FRONTEND_PID=$!

echo "Backend PID: $BACKEND_PID, Frontend PID: $FRONTEND_PID"
echo "Press Ctrl+C to stop both."

wait


