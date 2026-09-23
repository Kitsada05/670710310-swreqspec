"""Create initial tables: slots, bookings, audit_logs

รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01
"""
from sqlalchemy import create_engine

# ใช้ import แบบ absolute เพื่อให้สามารถโหลดไฟล์ migration โดยตรงใน test ได้
from backend.app.db.models import metadata


def upgrade(engine):
    # engine: SQLAlchemy Engine
    metadata.create_all(bind=engine)


def downgrade(engine):
    metadata.drop_all(bind=engine)
