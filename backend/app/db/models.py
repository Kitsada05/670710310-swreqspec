from sqlalchemy import Table, Column, Integer, String, Date, Time, DateTime, MetaData

# รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01
# ประกาศสคีม่า SQLAlchemy แบบ declarative-less เพื่อใช้งานกับ migration function
metadata = MetaData()

slots = Table(
    "slots",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("slot_date", Date, nullable=False),
    Column("start_time", Time, nullable=False),
    Column("package_code", String(50), nullable=False),
    Column("capacity", Integer, nullable=False, default=0),
    Column("remaining", Integer, nullable=False, default=0),
)

bookings = Table(
    "bookings",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("hn", String(64), nullable=False),
    Column("slot_id", Integer, nullable=False),
    Column("booking_date", DateTime, nullable=False),
    Column("queue_no", String(32), nullable=True),
    Column("status", String(20), nullable=False, default="confirmed"),
    Column("created_at", DateTime, nullable=False),
)

# audit_logs เก็บ actor_id, action, hn, accessed_at
audit_logs = Table(
    "audit_logs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("actor_id", String(64), nullable=False),
    Column("action", String(128), nullable=False),
    Column("hn", String(64), nullable=True),
    Column("accessed_at", DateTime, nullable=False),
)
