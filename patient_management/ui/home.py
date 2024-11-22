import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import logging
from ..utils.logging_config import setup_logging
from ..database.patient_db_access import db_load_patients
from .add_patient_form import AddPatientForm
from .add_evaluation_form import AddEvaluationForm
from .home_calendar_panel import CalendarPanel, get_appointments_for_date
from .create_report_window import CreateReportWindow

# Call this early on
setup_logging()
logger = logging.getLogger(__name__)

class Home:
    def __init__(self, master):
        self.master = master
        self.master.title("Patient Management System")

        # Set desired window size
        window_width = 700
        window_height = 430

        # Get screen dimensions and calculate coordinates to center the window
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the window geometry to be centered on the screen
        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")
        #TODO: change get_appointments_for_date for real db call function
        self.calendar = CalendarPanel(self.master, get_appointments_for_date)
        self.calendar.pack(padx=10, pady=10)

        # Frame for the patient list
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Patient List
        self.patient_list = ttk.Treeview(self.frame, columns=("Full Name", "Registry Number"), show='headings')
        self.patient_list.heading("Full Name", text="Full Name")
        self.patient_list.heading("Registry Number", text="Registry Number")
        self.patient_list.column("Full Name", anchor=tk.CENTER, width=200)
        self.patient_list.column("Registry Number", anchor=tk.CENTER, width=120)
        self.patient_list.pack()

        # Buttons Frame
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=10)

        self.create_appointment_button = tk.Button(self.buttons_frame, text="Create Appointment", command=self.create_appointment)
        self.create_appointment_button.grid(row=0, column=0, padx=5)

        self.add_patient_button = tk.Button(self.buttons_frame, text="Add Patient", command=self.add_patient)
        self.add_patient_button.grid(row=0, column=1, padx=5)

        self.edit_patient_button = tk.Button(self.buttons_frame, text="Edit Patient", command=self.edit_patient)
        self.edit_patient_button.grid(row=0, column=2, padx=5)

        self.save_evaluation_button = tk.Button(self.buttons_frame, text="Save Evaluation", command=self.save_evaluation)
        self.save_evaluation_button.grid(row=0, column=3, padx=5)

        self.create_report_button = tk.Button(self.buttons_frame, text="Create Report", command=self.create_report)
        self.create_report_button.grid(row=0, column=4, padx=5)

        # Load existing patients from the database
        self.load_patients()

    def load_patients(self):
        """Load all patients from the database and display them in the listbox."""
        patients = db_load_patients()  # Fetch the patient data

        if self.patient_list.get_children():
            for patient_list_child in self.patient_list.get_children():
                self.patient_list.delete(patient_list_child)
        
        # Insert each patient into the listbox
        for patient in patients:
            self.patient_list.insert("", tk.END, values=(patient[1], patient[2]))  # full_name is column 1, Registry_number is column 2


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
            self.load_patients()

        # Bind the close event of the popup to the on_close function
        add_patient_window.protocol("WM_DELETE_WINDOW", on_close)

        AddPatientForm(add_patient_window, self.master)

    def edit_patient(self):
        """Edit patient button action."""
        messagebox.showinfo("Edit Patient", "Edit Patient functionality will be implemented in the future.")

    def save_evaluation(self):
         # Check if a patient is selected
        selected_item = self.patient_list.selection()
        if not selected_item:
            messagebox.showwarning("No Patient Selected", "Please select a patient to add an evaluation.")
            return  # Exit the function if no patient is selected
        # Disable the home window
        self.master.attributes('-disabled', True)
        patient_name = selected_item[0]
        # Create a new window for Add Patient Form
        save_evaluation_window = AddEvaluationForm(self.master, patient_name)
        #save_evaluation_window.geometry("800x600")  # Set the size of the popup

        # Ensure modal behavior (focus remains on the popup)
        save_evaluation_window.grab_set()

        # Re-enable the home window once the popup is closed
        def on_close():
            save_evaluation_window.grab_release()
            self.master.attributes('-disabled', False)
            save_evaluation_window.destroy()

        # Bind the close event of the popup to the on_close function
        save_evaluation_window.protocol("WM_DELETE_WINDOW", on_close)

    def create_report(self):
        """Open the Create Report window if a patient is selected."""
        selected_patient_tree_id = self.patient_list.selection()
        if not selected_patient_tree_id:
            messagebox.showwarning("No Patient Selected", "Please select a patient to create a report.")
            return# Exit the function if no patient is selected
        selected_patient = self.patient_list.item(selected_patient_tree_id)['values']
        # Disable the home window
        self.master.attributes('-disabled', True)
        # Pass the selected patient (name, registry_number) to the CreateReportWindow
        create_report_window = CreateReportWindow(self.master, selected_patient)

        create_report_window.grab_set()

        # Re-enable the home window once the popup is closed
        def on_close():
            create_report_window.grab_release()
            self.master.attributes('-disabled', False)
            create_report_window.destroy()
        
        create_report_window.protocol("WM_DELETE_WINDOW", on_close)

    def create_appointment(self):
        """Create appointment button action."""
        messagebox.showinfo("Create Apointment", "Create Appointment functionality will be implemented.")

