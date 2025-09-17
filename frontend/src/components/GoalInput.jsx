// Reusable input for entering a learning goal

import { useState } from 'react';

export default function GoalInput({ onSubmit }) {
  const [value, setValue] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit?.(value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={value}
        placeholder="What do you want to learn?"
        onChange={(e) => setValue(e.target.value)}
        style={{ width: '100%', padding: '0.75rem', fontSize: '1rem' }}
      />
      <button type="submit" style={{ marginTop: '0.75rem' }}>Submit</button>
    </form>
  );
}


