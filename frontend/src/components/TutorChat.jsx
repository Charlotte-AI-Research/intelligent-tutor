// Simple chat UI placeholder for tutor interactions

import { useState } from 'react';

export default function TutorChat() {
  const [messages, setMessages] = useState([{ role: 'system', text: 'Hi! Ask me anything.' }]);
  const [input, setInput] = useState('');

  const send = () => {
    if (!input.trim()) return;
    setMessages([...messages, { role: 'user', text: input }, { role: 'assistant', text: 'This is a placeholder reply.' }]);
    setInput('');
  };

  return (
    <div>
      <div style={{ height: 200, overflow: 'auto', border: '1px solid #ddd', padding: 8 }}>
        {messages.map((m, i) => (
          <div key={i}><strong>{m.role}:</strong> {m.text}</div>
        ))}
      </div>
      <div style={{ marginTop: 8 }}>
        <input value={input} onChange={(e) => setInput(e.target.value)} />
        <button onClick={send}>Send</button>
      </div>
    </div>
  );
}


