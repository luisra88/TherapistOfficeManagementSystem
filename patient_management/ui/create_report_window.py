import tkinter as tk
from tkinter import ttk, messagebox
from ..database.patient_db_access import get_patient_evaluations_by_registry

class CreateReportWindow(tk.Toplevel):
    def __init__(self, parent, patient):
        super().__init__(parent)
        self.title("Create Report")
        self.geometry("400x300")
        self.patient = patient
        self.patient_registry = str(patient[1])
        self.evaluations = get_patient_evaluations_by_registry(self.patient_registry)

        # Display patient name
        tk.Label(self, text=f"Patient: {self.patient[0]}", font=("Arial", 12)).pack(pady=10)

        # Dropdown for evaluations
        tk.Label(self, text="Select Evaluation:").pack(pady=5)
        self.evaluation_var = tk.StringVar()
        self.evaluation_dropdown = ttk.Combobox(self, textvariable=self.evaluation_var)
        self.evaluation_dropdown['values'] = [e['evaluation_date'] for e in self.evaluations]
        self.evaluation_dropdown.pack(pady=5)

        # Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        self.create_button = tk.Button(button_frame, text="Create Report", command=self.create_report)
        self.create_button.grid(row=0, column=0, padx=10)
        
        self.cancel_button = tk.Button(button_frame, text="Cancel", command=self.destroy)
        self.cancel_button.grid(row=0, column=1, padx=10)

    def create_report(self):
        """Handle the report creation."""
        selected_evaluation = self.evaluation_var.get()
        if not selected_evaluation:
            messagebox.showwarning("No Evaluation Selected", "Please select an evaluation.")
            return

        # Implement the logic for creating the report here
        messagebox.showinfo("Success", f"Report for {self.patient['name']} using {selected_evaluation} created!")
        self.destroy()
