Feature: จองคิวตรวจสุขภาพ
Spec ID: SPEC-BKG-001
อ้างอิง: plan.md
วันที่: 2569-09-23

สรุป: ทำ 12 tasks, มี 1 task ที่รอ Open Questions

### T-01 สร้างตารางฐานข้อมูลและ migration
- รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-xx
- ไฟล์ที่แตะ: backend/app/db/models.py, backend/app/db/migrations/001_init.py
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: สามารถรัน migration และสร้างตาราง `slots`, `bookings`, `audit_logs` ใน SQLite memory ได้ (test fixture ผ่าน)
- สถานะ: พร้อมทำ

### T-02 เขียน API GET /slots สำหรับค้นช่วงว่าง
- รองรับ: FR-BKG-01, FR-BKG-06, NFR-PERF-01
- ตรวจด้วย: AC-BKG-05 (performance test ย่อส่วน) และ test_ GET_slots ที่ตรวจว่า response มี remaining
- ไฟล์ที่แตะ: backend/app/slots/router.py, backend/app/slots/service.py, backend/tests/test_slots.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: `GET /slots` ให้ผลลัพธ์รายการช่วงเวลาและ `remaining` ถูกต้อง (unit test ผ่าน)
- สถานะ: พร้อมทำ

### T-03 เขียน API POST /bookings พื้นฐาน (บันทึกการจอง และตัดที่นั่ง)
- รองรับ: FR-BKG-04
- ตรวจด้วย: AC-BKG-01
- ไฟล์ที่แตะ: backend/app/booking/router.py, backend/app/booking/service.py, backend/tests/test_booking_create.py
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: POST /bookings สร้าง booking ใน DB และ `remaining` ลดลงตามที่คาด (test_AC_BKG_01 ผ่าน)
- สถานะ: พร้อมทำ

### T-04 ป้องกันการจองซ้ำวันเดียวกัน (FR-BKG-02)
- รองรับ: FR-BKG-02
- ตรวจด้วย: AC-BKG-02
- ไฟล์ที่แตะ: backend/app/booking/service.py, backend/tests/test_booking_duplicate.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: เมื่อมี booking เดิมในวันเดียวกัน ระบบตอบปฏิเสธและคืนหมายเลขคิวเดิม (test_AC_BKG_02 ผ่าน)
- สถานะ: พร้อมทำ

### T-05 เสนอช่วงเวลาใกล้เคียงเมื่อช่วงเต็ม (FR-BKG-03)
- รองรับ: FR-BKG-03
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: backend/app/booking/service.py, backend/app/slots/service.py, backend/tests/test_booking_conflict.py
- ต้องทำหลัง: T-03, T-04
- เสร็จเมื่อ: เมื่อ POST /bookings พบช่วงเต็ม ให้ 409 พร้อม list 3 ช่วงที่ใกล้ที่สุด (AC-BKG-03 test ผ่าน)
- สถานะ: พร้อมทำ

### T-06 คิวส่งข้อความแบบ asynchronous และนโยบายส่งซ้ำ (notify/queue)
- รองรับ: IF-NOT-01, FR-BKG-05, NFR-REL-02, ASM-03
- ตรวจด้วย: AC-BKG-04
- ไฟล์ที่แตะ: backend/app/notify/queue.py, backend/app/booking/service.py, backend/tests/test_notify_queue.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: POST /bookings วางงานส่งข้อความลงคิวทันที และเมื่อส่งไม่สำเร็จ ระบบบันทึกงานส่งซ้ำตามนโยบายภายใน 5 นาที (AC-BKG-04 ผ่าน)
- สถานะ: พร้อมทำ

### T-07 audit log middleware และ test (DOM-PDPA-01)
- รองรับ: DOM-PDPA-01
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: backend/app/audit/middleware.py, backend/app/db/models.py (audit_logs), backend/tests/test_audit_log.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: การเรียกดูการจองสร้าง `audit_logs` ระบุ `actor_id`, `accessed_at`, `hn` (AC-BKG-06 ผ่าน)
- สถานะ: พร้อมทำ

### T-08 HIS lookup endpoint (IF-HIS-01)
- รองรับ: IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ (เป็นอินเทอร์เฟซ) แต่ใช้งานร่วมกับการสร้าง booking
- ไฟล์ที่แตะ: backend/app/his/client.py, backend/app/booking/service.py, backend/tests/test_his_lookup.py
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: GET /patients/lookup คืนค่า `hn` จากเลขบัตร โดยไม่บันทึกเลขบัตรใน `bookings` (unit test ผ่าน)
- สถานะ: พร้อมทำ

### T-09 หน้าจอ: หน้าเลือกแพ็กเกจและช่วงเวลา (SlotPicker)
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ (หน้าจอ) แต่มี test หน้าจอย่อยตาม AC-BKG-03.test.jsx
- ไฟล์ที่แตะ: frontend/src/pages/SlotPicker.jsx, frontend/src/__tests__/SlotPicker.test.jsx
- ต้องทำหลัง: ไม่มี (ใช้ API จำลองได้)
- เสร็จเมื่อ: หน้าจอเรียก `GET /slots` (หรือ client mock) แล้วแสดงช่วงเวลาและ `remaining` (หน้าจอ unit test ผ่าน)
- สถานะ: พร้อมทำ
- สถานะ: เสร็จ รอทีมตรวจ

### T-10 หน้าจอ: หน้ายืนยันการจอง (ConfirmBooking)
- รองรับ: FR-BKG-03, FR-BKG-04
- ตรวจด้วย: AC-BKG-03 (หน้าจอ) และ AC-BKG-01 (หากเชื่อม API จริง)
- ไฟล์ที่แตะ: frontend/src/pages/ConfirmBooking.jsx, frontend/src/__tests__/ConfirmBooking.test.jsx
- ต้องทำหลัง: T-09
- เสร็จเมื่อ: เมื่อ API จำลองตอบ 409 หน้าจอแสดงข้อความ "ช่วงเวลาเต็ม" และ 3 ปุ่มตัวเลือก (test AC-BKG-03.test.jsx ผ่าน)
- สถานะ: พร้อมทำ

### T-11 หน้าจอ: หน้าแสดงผลการจอง (BookingResult)
- รองรับ: FR-BKG-04, FR-BKG-05
- ตรวจด้วย: AC-BKG-01 (แสดง queue_no) และ AC-BKG-04 (แสดงหมายเลขคิว แม้ notify ล้มเหลว)
- ไฟล์ที่แตะ: frontend/src/pages/BookingResult.jsx, frontend/src/__tests__/BookingResult.test.jsx
- ต้องทำหลัง: T-10, T-03
- เสร็จเมื่อ: หน้าจอแสดงหมายเลขคิวทันทีแม้ระบบแจ้งเตือนไม่ตอบ (unit test ผ่าน)
- สถานะ: พร้อมทำ

### T-12 จัดการการออก `queue_no` (รอ Q-02)
- รองรับ: FR-BKG-04 (แสดง queue_no) แต่รูปแบบยังเป็น Open Question (Q-02)
- ตรวจด้วย: ไม่มี AC ตรง ๆ จนกว่า Q-02 จะตอบ แต่ต้องมีช่องเก็บ `queue_no` และ API คืนค่า `queue_no` ถ้ามี
- ไฟล์ที่แตะ: backend/app/db/models.py (bookings.queue_no), backend/app/booking/service.py
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: มีการเก็บ `queue_no` ในตาราง แต่กลไกการกำหนดเลขยัง `รอ Q-02` (สถานะ รอ Q-02)
- สถานะ: รอ Q-02

---

ตารางตรวจความครบ: AC -> task

| AC ID | task ที่ตรวจ AC นี้ |
|---|---|
| AC-BKG-01 | T-03, T-11 |
| AC-BKG-02 | T-04 |
| AC-BKG-03 | T-05, T-10 |
| AC-BKG-04 | T-06, T-11 |
| AC-BKG-05 | T-02 |
| AC-BKG-06 | T-07 |

ตารางตรวจความครบ: Constraint -> task

| Constraint ID | task ที่ทำให้เป็นจริง |
|---|---|
| CON-TECH-01 | T-01 |
| DOM-PDPA-01 | T-01, T-07 |
| IF-IDP-01 | (ถูกตรวจในทุก endpoint ผ่าน auth/idp.py) |
| IF-HIS-01 | T-01, T-08 |
| IF-NOT-01 | T-06 |

สิ่งที่ยังไม่ทำ (Open Questions)

- Q-02: รูปแบบและนโยบายการรีเซ็ตหมายเลขคิว (รอเจ้าหน้าที่เวชระเบียน)
  - Task ที่รอ: T-12
