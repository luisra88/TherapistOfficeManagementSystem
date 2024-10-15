import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import logging
from ..utils.logging_config import setup_logging
from ..database.patient_db_access import db_load_patients
from .add_patient_form import AddPatientForm
from .add_evaluation_form import AddEvaluationForm

# Call this early on
setup_logging()
logger = logging.getLogger(__name__)

class Home:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Management System")

        # Frame for the patient list
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Patient List
        self.patient_list = ttk.Treeview(self.frame, columns=("Full Name", "Registry Number"), show='headings')
        self.patient_list.heading("Full Name", text="Full Name")
        self.patient_list.heading("Registry Number", text="Registry Number")
        self.patient_list.column("Full Name", anchor=tk.CENTER, width=200)
        self.patient_list.column("Registry Number", anchor=tk.CENTER, width=100)
        self.patient_list.pack()

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=10)

        self.add_patient_button = tk.Button(self.buttons_frame, text="Add Patient", command=self.add_patient)
        self.add_patient_button.grid(row=0, column=0, padx=5)

        self.edit_patient_button = tk.Button(self.buttons_frame, text="Edit Patient", command=self.edit_patient)
        self.edit_patient_button.grid(row=0, column=1, padx=5)

        self.save_evaluation_button = tk.Button(self.buttons_frame, text="Save Evaluation", command=self.save_evaluation)
        self.save_evaluation_button.grid(row=0, column=2, padx=5)

        self.create_report_button = tk.Button(self.buttons_frame, text="Create Report", command=self.create_report)
        self.create_report_button.grid(row=0, column=3, padx=5)

        # Load existing patients from the database
        self.load_patients()

    def load_patients(self):
        """Load all patients from the database and display them in the listbox."""
        """
        patients = db_load_patients()  # Fetch the patient data
        
        # Clear the listbox before inserting new items
        self.listbox.delete(0, tk.END)
        
        # Insert each patient into the listbox
        for patient in patients:
            self.listbox.insert(tk.END, f"{patient[0]} - {patient[1]}")  # Assuming patient_id, full_name are columns
            """
        
        # Placeholder: Replace with actual database fetching logic
        patients = [
            ("John Doe", "REG123"),
            ("Jane Smith", "REG456"),
            ("Alice Johnson", "REG789"),
        ]
        for patient in patients:
            self.patient_list.insert("", "end", values=patient)


    def add_patient(self):
        # Disable the home window
        self.master.attributes('-disabled', True)
        
        # Create a new window for Add Patient Form
        add_patient_window = tk.Toplevel(self.master)
        add_patient_window.geometry("800x600")  # Set the size of the popup

        # Ensure modal behavior (focus remains on the popup)
        add_patient_window.grab_set()

        # Re-enable the home window once the popup is closed
        def on_close():
            add_patient_window.grab_release()
            self.master.attributes('-disabled', False)
            add_patient_window.destroy()

        # Bind the close event of the popup to the on_close function
        add_patient_window.protocol("WM_DELETE_WINDOW", on_close)

        AddPatientForm(add_patient_window, self.master)

    def edit_patient(self):
        """Edit patient button action."""
        messagebox.showinfo("Edit Patient", "Edit Patient functionality will be implemented.")

    def save_evaluation(self):
         # Check if a patient is selected
        selected_item = self.patient_list.selection()
        if not selected_item:
            messagebox.showwarning("No Patient Selected", "Please select a patient to add an evaluation.")
            return  # Exit the function if no patient is selected
         # Disable the home window
        self.master.attributes('-disabled', True)
        
        # Create a new window for Add Patient Form
        save_evaluation_window = tk.Toplevel(self.master)
        save_evaluation_window.geometry("800x600")  # Set the size of the popup

        # Ensure modal behavior (focus remains on the popup)
        save_evaluation_window.grab_set()

        # Re-enable the home window once the popup is closed
        def on_close():
            save_evaluation_window.grab_release()
            self.master.attributes('-disabled', False)
            save_evaluation_window.destroy()

        # Bind the close event of the popup to the on_close function
        save_evaluation_window.protocol("WM_DELETE_WINDOW", on_close)

        patient_name = selected_item[0]

        AddEvaluationForm(save_evaluation_window, self.master, patient_name)

    def create_report(self):
        """Create report button action."""
        messagebox.showinfo("Create Report", "Create Report functionality will be implemented.")

if __name__ == "__main__":
    master = tk.Tk()
    app = Home(master)
    master.mainloop()
