// Visual card for content items

export default function ContentCard({ title, type }) {
  return (
    <div style={{ border: '1px solid #eee', padding: '0.75rem', borderRadius: 8 }}>
      <h4 style={{ margin: 0 }}>{title}</h4>
      <small>{type}</small>
    </div>
  );
}


