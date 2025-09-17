// Landing page: enter learning goal
// This simple page provides a text input and button for submitting a goal.

import { useState } from 'react';

export default function IndexPage() {
  const [goal, setGoal] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Goal submitted: ${goal}`);
  };

  return (
    <div style={{ maxWidth: 640, margin: '2rem auto', padding: '1rem' }}>
      <h1>Intelligent Tutor</h1>
      <p>Enter your learning goal to get started.</p>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={goal}
          placeholder="e.g., Learn Python for data science"
          onChange={(e) => setGoal(e.target.value)}
          style={{ width: '100%', padding: '0.75rem', fontSize: '1rem' }}
        />
        <button type="submit" style={{ marginTop: '1rem', padding: '0.5rem 1rem' }}>
          Submit Goal
        </button>
      </form>
    </div>
  );
}


