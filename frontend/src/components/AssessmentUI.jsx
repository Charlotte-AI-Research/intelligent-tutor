// Minimal assessment UI placeholder

import { useState } from 'react';

export default function AssessmentUI() {
  const [answer, setAnswer] = useState('');
  return (
    <div>
      <p>Question: What is a variable?</p>
      <textarea value={answer} onChange={(e) => setAnswer(e.target.value)} />
      <div>
        <button onClick={() => alert('Submitted!')}>Submit</button>
      </div>
    </div>
  );
}


