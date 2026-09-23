import React, { useEffect, useState } from "react";

// รองรับ: FR-BKG-01, FR-BKG-06
export default function SlotPicker() {
  const [slots, setSlots] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let mounted = true;
    // เรียก API ตามสัญญาใน plan: GET /slots
    fetch("/api/slots")
      .then((r) => {
        if (!r.ok) throw new Error("fetch failed");
        return r.json();
      })
      .then((data) => {
        if (mounted) setSlots(Array.isArray(data) ? data : []);
      })
      .catch((err) => {
        if (mounted) setError(err.message || "error");
      })
      .finally(() => {
        if (mounted) setLoading(false);
      });
    return () => (mounted = false);
  }, []);

  if (loading) return <div>Loading slots…</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h2>Available slots</h2>
      {slots.length === 0 ? (
        <div>No slots available</div>
      ) : (
        <ul>
          {slots.map((s) => (
            <li key={s.id} data-testid={`slot-${s.id}`}>
              {s.slot_date} {s.start_time} — remaining: {s.remaining}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
