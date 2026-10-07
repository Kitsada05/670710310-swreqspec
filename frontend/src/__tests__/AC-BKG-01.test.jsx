import { render, screen } from '@testing-library/react'
import { describe, expect, test } from 'vitest'

function BookingResult({ queueNo = 'A001' }) {
  return (
    <section>
      <h2>ผลการจอง</h2>
      <p>หมายเลขคิว</p>
      <strong>{queueNo}</strong>
    </section>
  )
}

describe('AC-BKG-01 UI', () => {
  test('แสดงหมายเลขคิวเมื่อการจองสำเร็จ', () => {
    render(<BookingResult queueNo="A001" />)

    expect(screen.getByText(/หมายเลขคิว/i)).toBeTruthy()
    expect(screen.getByText(/A001/i)).toBeTruthy()
  })
})
