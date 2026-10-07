# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 08:40 | test: 7 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | ไม่มี AC | T-02 | backend/app/slots/service.py: list_available_slots; backend/app/slots/router.py: get_slots | test_AC_BKG_05 (ผ่าน) | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 (พร้อมทำ) | ไม่มี | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 (พร้อมทำ) | ไม่มี | ไม่มี | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/service.py: create_booking; backend/app/booking/router.py: create_booking | test_TC_BKG_01_1_success, test_TC_BKG_01_2_boundary_remaining_one (ผ่าน) | ช่องโหว่ |
| FR-BKG-05 | AC-BKG-04 | T-07 (พร้อมทำ) | ไม่มี | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-10, T-12 (พร้อมทำ) | backend/app/slots/service.py: list_available_slots (กรอง package_code) | ไม่มี | ยังไม่ถึง |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py: list_available_slots | test_AC_BKG_05 (ผ่าน) | ครบ |
| NFR-SEC-01 | ไม่มี AC | ไม่มี task | ไม่มี | ไม่มี | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 (พร้อมทำ) | ไม่มี | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | ไม่มี task | ไม่มี | ไม่มี | ยังไม่ถึง |
| CON-TECH-01 | ไม่มี AC | T-01 | backend/app/config.py: DATABASE_URL; backend/app/db/session.py: get_db | test_T01_schema.py (ผ่าน) | ช่องโหว่ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 (พร้อมทำ) | backend/app/db/models.py: AuditLog (ตาราง) | ไม่มี | ยังไม่ถึง |
| IF-IDP-01 | ไม่มี AC | T-03 | backend/app/auth/idp.py: get_verified_hn | test_TC_BKG_01_1_success, test_TC_BKG_01_2_boundary_remaining_one (ผ่าน) | ครบ |
| IF-HIS-01 | ไม่มี AC | T-09 (พร้อมทำ) | backend/app/db/models.py: Booking (ไม่มี national_id); backend/app/booking/router.py: BookingRequest.national_id | test_T01_no_national_id (ผ่าน) | ช่องโหว่ |
| IF-NOT-01 | AC-BKG-04 | T-07 (พร้อมทำ) | ไม่มี | ไม่มี | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/service.py: list_available_slots | FR-BKG-01 | ไม่ตรง | ตัวเลข `DAYS_AHEAD = 14` แทน 30 วัน ตาม spec; ระยะเวลาที่แสดงสั้นกว่า requirement อย่างชัดเจน |
| backend/app/booking/service.py: create_booking | FR-BKG-04 | ไม่ตรง | ตรวจ `slot.remaining < 0` แทน `<= 0` จึงยังอนุญาตให้จองเมื่อ remaining = 0 ได้; เป็นช่องโหว่ต่อ FR-BKG-03 / AC-BKG-01 |
| backend/app/booking/service.py: next_queue_no | Q-02 | ไม่ตรง | ใช้รูปแบบ `A001` โดยไม่ได้รอคำตอบ Q-02; เป็นการเดาแทนทีมที่ยังไม่ได้ตัดสิน |
| backend/app/booking/router.py: BookingRequest.national_id และ logger.info("... national_id=%s") | IF-HIS-01 | ไม่ตรง | ข้อมูลเลขบัตรประชาชนยังถูกส่งผ่าน request model และ log แม้จะไม่เก็บลงตารางการจอง แต่ยังไม่ปกป้องข้อมูลตาม constraint |
| backend/app/config.py: DATABASE_URL | CON-TECH-01 | ไม่ตรง | ค่าเริ่มต้นคือ SQLite (`sqlite:///./dev.db`) แม้ comments ระบุ PostgreSQL สำหรับระบบจริง แต่โค้ดจะรันเป็น SQLite โดย default หากไม่ได้ตั้ง env |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-001 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py: DAYS_AHEAD = 14 | FR-BKG-01 | ระยะเวลาที่แสดงถูกจำกัดที่ 14 วัน ขณะที่ spec ระบุ 30 วันข้างหน้า | แก้โค้ด |
| F-002 | เดา Q-xx | backend/app/booking/service.py: next_queue_no | Q-02, FR-BKG-04 | โค้ดสร้างหมายเลขคิวเป็น `A001` แบบเดาโดยไม่รอคำตอบจากเจ้าหน้าที่เวชระเบียน | เพิ่ม Q-xx |
| F-003 | ละเมิด Constraint | backend/app/booking/router.py: BookingRequest.national_id + logger.info | IF-HIS-01 | Data model และ log ยังรับ/พิมพ์เลขบัตรประชาชน จึงไม่เป็นการปกป้องข้อมูลตาม constraint ที่ห้ามเก็บ | แก้โค้ด |
| F-004 | โค้ดไม่มี FR | backend/app/booking/service.py: create_booking | FR-BKG-03, AC-BKG-01 | เมื่อ `remaining == 0` โค้ดยังยอมจองได้ เพราะเงื่อนไขเป็น `< 0` แทน `<= 0` และไม่มีโค้ดให้เสนอ 3 ช่วงที่ว่าง | แก้โค้ด |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
| - | ไม่มี | ไม่มีข้อค้นพบเก่าที่แก้แล้วในรอบนี้ |
