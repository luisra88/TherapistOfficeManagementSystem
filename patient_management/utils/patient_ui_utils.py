import tkinter as tk
from tkcalendar import DateEntry
from datetime import date

def add_field(frame, label_text, row, col, widgets, widget_name):
    """Helper function to create and place a label and entry widget."""
    tk.Label(frame, text=label_text).grid(row=row, column=col, sticky="w")
    entry = tk.Entry(frame)
    entry.grid(row=row, column=col + 1)
    widgets[widget_name] = entry

def add_date_entry(frame, label_text, row, col, widgets, widget_name):
    """Create and place a label and DateEntry widget."""
    tk.Label(frame, text=label_text).grid(row=row, column=col, sticky="w")
    date_entry = DateEntry(frame, date_pattern='yyyy-mm-dd', showweeknumbers=False, maxdate=date.today())
    date_entry.grid(row=row, column=col + 1)
    widgets[widget_name] = date_entry