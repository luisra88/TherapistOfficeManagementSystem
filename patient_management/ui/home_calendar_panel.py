import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class DayPanel(tk.Frame):
    """A single day panel representing a day in the calendar."""
    def __init__(self, parent, date, get_appointments_func=None, is_current_day=False):
        super().__init__(parent, bg="#ADD8E6", bd=1, relief="solid")
        self.date = date
        self.is_current_day = is_current_day
        self.get_appointments_func = get_appointments_func
        self.appts = []  # Default empty list for appointments

        # Highlight current day
        if self.is_current_day:
            self.config(bg="#5f9ea0")

        # Date label
        date_label = tk.Label(self, text=date.strftime("%A\n%d %b"), font=("Arial", 10, "bold"), bg=self["bg"])
        date_label.pack(pady=(5, 2))

        # Appointment summary
        self.appt_summary = tk.Label(self, text="No Appointments", font=("Arial", 8), bg=self["bg"], wraplength=100)
        self.appt_summary.pack(pady=(0, 5))

        # Click event
        self.bind("<Button-1>", self.show_details)
        date_label.bind("<Button-1>", self.show_details)
        self.appt_summary.bind("<Button-1>", self.show_details)

        # Fetch and display appointments for this day
        self.fetch_appointments()

    def fetch_appointments(self):
        """Fetch appointments from an external source."""
        if self.get_appointments_func:
            self.appts = self.get_appointments_func(self.date)
            if self.appts:
                self.appt_summary.config(text=f"{len(self.appts)} Appointments")
            else:
                self.appt_summary.config(text="No Appointments")

    def show_details(self, event=None):
        """Show detailed appointment information in a messagebox."""
        details = f"Appointments on {self.date.strftime('%A, %d %b')}:\n"
        details += "\n".join(f"- {appt}" for appt in self.appts) if self.appts else "No appointments"
        messagebox.showinfo("Appointments", details)


class CalendarPanel(tk.Frame):
    """A calendar view widget showing seven days, centered on the current day."""
    def __init__(self, parent, get_appointments_func):
        super().__init__(parent)
        self.pack(fill="x", padx=10, pady=10)

        # Current date
        self.today = datetime.now().date()
        self.days = []

        # Create the day panels
        for i in range(-2, 5):  # 2 days before to 4 days after
            day_date = self.today + timedelta(days=i)
            is_current_day = (i == 0)
            day_panel = DayPanel(self, day_date, get_appointments_func, is_current_day)
            day_panel.pack(side="left", fill="y", expand=True, padx=2, pady=2)
            self.days.append(day_panel)


# Example usage
def get_appointments_for_date(date):
    """Simulate fetching appointments for a specific date."""
    appointments_by_date = {
        datetime.now().date(): ["Dentist - 10 AM", "Lunch with John - 1 PM"],
        datetime.now().date() + timedelta(days=1): ["Project Meeting - 3 PM"],
        datetime.now().date() - timedelta(days=1): ["Yoga Class - 7 AM"]
    }
    return appointments_by_date.get(date, [])
