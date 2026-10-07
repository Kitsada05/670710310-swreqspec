# AC-BKG-01 (FR-BKG-04)
import pytest

from app.db.models import Slot
from tests.conftest import AUTH


def test_TC_BKG_01_1_success(client, db, make_slot):
    """TC-BKG-01-1: ทางปกติ - ยืนยันตัวตนแล้วและมีที่นั่งว่าง 1 ที่"""
    # Given: ยืนยันตัวตนแล้ว และช่วง 09.00 น. มีที่นั่งว่าง 1 ที่
    slot = make_slot(start="09:00", remaining=1)

    # When: ยืนยันการจอง
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then: บันทึกสำเร็จ
    assert res.status_code == 201
    data = res.json()
    assert data["slot_id"] == slot.id
    assert data["queue_no"] is not None

    # Then: แสดงหมายเลขคิว (รอ Q-02) - ยังไม่ assert รูปแบบจริงเพราะยังไม่มีคำตอบจากเจ้าหน้าที่เวชระเบียน
    # Then: ที่นั่งว่างของช่วงนั้นเป็น 0
    saved_slot = db.get(Slot, slot.id)
    assert saved_slot.remaining == 0


def test_TC_BKG_01_2_boundary_remaining_one(client, db, make_slot):
    """TC-BKG-01-2: ขอบ - ช่วงที่มีที่นั่งว่างขั้นต่ำก่อนยืนยัน"""
    # Given: ยืนยันตัวตนแล้ว และช่วง 09.00 น. มีที่นั่งว่าง 1 ที่ (ขั้นต่ำก่อนยืนยัน)
    slot = make_slot(start="09:00", remaining=1)

    # When: ยืนยันการจอง
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then: บันทึกสำเร็จ
    assert res.status_code == 201
    data = res.json()
    assert data["slot_id"] == slot.id

    # Then: แสดงหมายเลขคิว (รอ Q-02)
    # Then: ที่นั่งว่างของช่วงนั้นเป็น 0
    saved_slot = db.get(Slot, slot.id)
    assert saved_slot.remaining == 0


@pytest.mark.skip(reason="ผลที่ต้องคืนเมื่อช่วงว่างเป็น 0 หรือยังไม่ยืนยันตัวตนยังไม่ชัดเจนใน AC-BKG-01 ต้องถามทีมก่อน assert")
def test_TC_BKG_01_3_invalid_state(client, make_slot):
    """TC-BKG-01-3: ทางผิด - เงื่อนไขใน Given ไม่เป็นจริง"""
    # Given: ยืนยันตัวตนแล้ว แต่ช่วง 09.00 น. มีที่นั่งว่าง 0 ที่ หรือยังไม่ยืนยันตัวตน
    # When: ยืนยันการจอง
    # Then: spec ไม่ได้บอก; ต้องถามว่าผลควรเป็นการปฏิเสธ/แจ้ง "ช่วงเวลาเต็ม" ตาม FR-BKG-03 หรือไม่
    pass
