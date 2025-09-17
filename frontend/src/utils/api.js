// Simple helper for backend calls

const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function getHealth() {
  const res = await fetch(`${BASE_URL}/health`);
  return res.json();
}

export async function listGoals() {
  const res = await fetch(`${BASE_URL}/goals/`);
  return res.json();
}


