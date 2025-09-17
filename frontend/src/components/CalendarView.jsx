// Simple calendar view placeholder

export default function CalendarView({ events = [] }) {
  return (
    <div>
      <h4>Upcoming</h4>
      <ul>
        {events.map((e, i) => (
          <li key={i}>{e.title} — {e.date || e.datetime}</li>
        ))}
      </ul>
    </div>
  );
}


