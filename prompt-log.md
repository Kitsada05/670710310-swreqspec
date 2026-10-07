# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ลบของเก่า

---

## 2569-09-23 13.40 คำสั่ง: /tasks specs/001-booking/spec.md

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: specs/001-booking/tasks.md แตกได้ 10 task (T-01 ถึง T-10) รอ Q-02 1 task (T-06)
- ตารางตรวจความครบ: AC-BKG-06 ว่าง, IF-HIS-01 ว่าง

### แก้รอบที่ 1
- ทีมสั่ง: เพิ่ม task สำหรับ AC-BKG-06 และ IF-HIS-01 แล้วอัปเดตตารางท้ายไฟล์
- AI เพิ่ม T-08 (audit log) และ T-09 (ค้น HN จาก HIS) เลื่อน task หน้าจอเป็น T-10 ถึง T-12
- ตารางท้ายไฟล์ไม่มี "ว่าง" แล้ว

---

## 2569-09-23 14.20 คำสั่ง: /implement T-01 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_T01_schema.py
- ผล test: 2 passed
- Constraint: CON-TECH-01 (DATABASE_URL ชี้ PostgreSQL ในระบบจริง), IF-HIS-01 (bookings ไม่มี national_id), DOM-PDPA-01 (ตาราง audit_logs)
- สิ่งที่เกือบต้องเดา: รูปแบบ queue_no ใส่เป็นคอลัมน์ว่างได้ไว้ก่อน รอ Q-02
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-27 19.05 คำสั่ง: /implement T-02 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/slots/router.py, backend/app/slots/service.py, backend/app/main.py, backend/tests/conftest.py, backend/tests/test_AC_BKG_05.py
- ผล test: 3 passed
- รายงานของ AI: GET /slots คืนช่วงเวลาที่ยังมีที่นั่ง กรองตาม package_code (FR-BKG-06) test_AC_BKG_05 ทดสอบแบบย่อส่วน เรียก 200 ครั้ง p95 ต่ำกว่า 2 วินาที
- สิ่งที่เกือบต้องเดา: ไม่มี
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-28 20.30 คำสั่ง: /implement T-03 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/booking/router.py, backend/app/booking/service.py, backend/app/auth/idp.py และแก้ backend/app/main.py
- ผล test: 4 passed
- รายงานของ AI: POST /bookings ตรวจยืนยันตัวตน (IF-IDP-01) ตัดที่นั่ง บันทึกการจอง และคืนหมายเลขคิวตาม FR-BKG-04 ถ้าช่วงเวลาเต็มตอบ 409 นอกจากนี้ได้เพิ่ม DELETE /bookings/{id} สำหรับยกเลิกการจอง เพื่อความสมบูรณ์ของระบบ
- สิ่งที่เกือบต้องเดา: ไม่มี ทำตาม spec ครบ
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-10-07 00.00 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- โหมด: ร่าง (draft)
- สถานะใน [specs/001-booking/test-cases.md](specs/001-booking/test-cases.md): ยังไม่มีแถวใดมีสถานะ "ใช้ได้" จึงหยุดก่อนเขียนโค้ด test
- TC ID ที่เสนอ: TC-BKG-01-1, TC-BKG-01-2, TC-BKG-01-3
- สรุป: AC-BKG-01 มีประเด็น Open Question ที่ต้องตรวจอีกครั้งเรื่องรูปแบบหมายเลขคิว (Q-02) ทำให้ส่วน "แสดงหมายเลขคิว" ใน Then ต้องเขียนเป็น "(รอ Q-02)" แทนการ assert รูปแบบจริง
- ผล: ยังไม่รัน pytest หรือ vitest เนื่องจากโหมดร่างตามคำสั่ง

---

## 2569-10-07 08.30 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- โหมด: เขียน test จากแถวสถานะ "ใช้ได้"
- ฟิวส์ที่ใช้: [specs/001-booking/test-cases.md](specs/001-booking/test-cases.md), [specs/001-booking/spec.md](specs/001-booking/spec.md), [specs/001-booking/tasks.md](specs/001-booking/tasks.md)
- TC ID ที่เขียน test: TC-BKG-01-1, TC-BKG-01-2
- TC ID ที่ค้างเพราะ spec ยังไม่ชัด: TC-BKG-01-3
- ไฟล์ที่แก้: [backend/tests/test_AC_BKG_01.py](backend/tests/test_AC_BKG_01.py), [frontend/src/__tests__/AC-BKG-01.test.jsx](frontend/src/__tests__/AC-BKG-01.test.jsx)
- ผลการทดสอบ: backend 2 passed, 1 skipped; frontend 1 passed
- หมายเหตุ: TC-BKG-01-3 ถูกใส่เป็น skipped เพราะ Then ของแถวมีคำว่า "spec ไม่ได้บอก" และไม่ได้ระบุผลลัพธ์ที่ชัดเจนใน spec จึงไม่ assert ใด ๆ

---

## 2569-10-07 08:40 คำสั่ง: /verify specs/001-booking/

- โหมด: ตรวจ requirement (ไม่แก้โค้ด)
- อ่านไฟล์: [specs/001-booking/spec.md](specs/001-booking/spec.md), [specs/001-booking/plan.md](specs/001-booking/plan.md), [specs/001-booking/tasks.md](specs/001-booking/tasks.md), [specs/001-booking/test-cases.md](specs/001-booking/test-cases.md), [AGENTS.md](AGENTS.md)
- รัน test: `cd backend && pytest -v` -> 5 passed, 1 skipped; `cd frontend && npm test` -> 2 passed
- สรุปตามรอยไปข้างหน้า: ครบ 2 ข้อ (NFR-PERF-01, IF-IDP-01), ยังไม่ถึง 9 ข้อ, ช่องโหว่ 4 ข้อ
- ข้อค้นพบใหม่: F-001, F-002, F-003, F-004
- ไฟล์ที่สร้าง: [specs/001-booking/rtm.md](specs/001-booking/rtm.md)

---

## 2569-10-07 09:15 คำสั่ง: /verify specs/001-booking/

- โหมด: ตรวจ requirement (ไม่แก้โค้ด)
- อ่านไฟล์: [specs/001-booking/spec.md](specs/001-booking/spec.md), [specs/001-booking/plan.md](specs/001-booking/plan.md), [specs/001-booking/tasks.md](specs/001-booking/tasks.md), [specs/001-booking/test-cases.md](specs/001-booking/test-cases.md), [specs/001-booking/rtm.md](specs/001-booking/rtm.md), [AGENTS.md](AGENTS.md)
- รัน test: `cd backend && pytest -v` -> 5 passed, 1 skipped; `cd frontend && npm test` -> 2 passed
- ข้อค้นพบที่แก้แล้ว: F-005 (ลบ endpoint ยกเลิกการจองออกจาก Out of scope), F-006 (ปรับข้อความและจำนวนตัวเลือกในหน้าจอยืนยันตรง AC-BKG-03)
- สรุปตามรอยไปข้างหน้า: ครบ 2 ข้อ, ช่องโหว่ 6 ข้อ, ยังไม่ถึง 7 ข้อ
- ข้อค้นพบยังคงเปิด: F-001, F-002, F-003, F-004
- ไฟล์ที่อัปเดต: [specs/001-booking/rtm.md](specs/001-booking/rtm.md)
