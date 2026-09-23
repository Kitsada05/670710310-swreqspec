import pathlib
import importlib.util
from sqlalchemy import create_engine, inspect


def load_migration_module():
    # โหลดไฟล์ migration ด้วย importlib โดยใช้ path เพื่อรองรับชื่อไฟล์ที่ขึ้นต้นด้วยตัวเลข
    migration_path = (
        pathlib.Path(__file__).resolve().parents[1]
        / "app" / "db" / "migrations" / "001_init.py"
    )
    spec = importlib.util.spec_from_file_location("m001", str(migration_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_migration_creates_tables():
    # ใช้ SQLite memory เป็น engine ทดสอบ
    engine = create_engine("sqlite:///:memory:")
    m001 = load_migration_module()
    m001.upgrade(engine)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert "slots" in tables
    assert "bookings" in tables
    assert "audit_logs" in tables

    # ตรวจคอลัมน์บางตัว
    cols = {c["name"] for c in inspector.get_columns("bookings")}
    assert "hn" in cols
    assert "queue_no" in cols
    assert "created_at" in cols
