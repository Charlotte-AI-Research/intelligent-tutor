## API Specification (MVP)

Base URL: `http://localhost:8000`

### GET /health
Response: `{ "status": "ok" }`

### Goals
- `GET /goals/` → `{ goals: string[] }`
- `POST /goals/` body `{ text: string }` → echoes back `{ message, goal }`

### Roadmap
- `GET /roadmap/` → `{ steps: { title: string, items: string[] }[] }`

### Content
- `GET /content/` → `{ items: { id: number, title: string, type: string }[] }`

### Assessments
- `POST /assessments/grade` body `{ question_id: number, answer: string }`
  → `{ question_id, score: number, feedback: string }`

### Profile
- `GET /profile/` → sample user profile JSON

### Calendar
- `GET /calendar/upcoming` → `{ events: { title: string, date: string }[] }`


