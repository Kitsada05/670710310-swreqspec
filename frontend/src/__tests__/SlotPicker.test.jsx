import { render, screen, waitFor } from "@testing-library/react";
import { vi } from "vitest";
import SlotPicker from "../pages/SlotPicker";

describe("SlotPicker", () => {
  beforeEach(() => {
    global.fetch = vi.fn(() =>
      Promise.resolve({
        ok: true,
        json: () =>
          Promise.resolve([
            { id: 1, slot_date: "2026-10-01", start_time: "09:00", remaining: 5 },
            { id: 2, slot_date: "2026-10-01", start_time: "10:00", remaining: 0 },
          ]),
      })
    );
  });

  afterEach(() => {
    vi.resetAllMocks();
    delete global.fetch;
  });

  test("renders slot list with remaining counts", async () => {
    render(<SlotPicker />);
    // loading text appears
    expect(screen.getByText(/Loading slots/i)).toBeTruthy();
    await waitFor(() => screen.getByText(/Available slots/i));
    const slot1 = screen.getByTestId("slot-1");
    const slot2 = screen.getByTestId("slot-2");
    expect(slot1.textContent).toContain("remaining: 5");
    expect(slot2.textContent).toContain("remaining: 0");
  });
});
