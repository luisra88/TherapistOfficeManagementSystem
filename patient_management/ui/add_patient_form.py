import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date

from . import patient_form_health_history
from ..utils.patient_manager import create_new_patient
from ..ui import patient_form_main, patient_form_evolution, patient_form_scholar_info, patient_form_prenatal, patient_form_postnatal, patient_form_health, patient_form_treatments, patient_form_scholar_history, patient_form_relationships, patient_form_behavior

class AddPatientForm:
    def __init__(self, root, parent):
        self.root = root
        self.root.withdraw()
        self.parent = parent

        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.geometry("300x100")  # Set size explicitly
        self.loading_window.resizable(False, False)
        self.loading_window.title("Loading...")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (300 // 2)
        y = (screen_height // 2) - (100 // 2)
        self.loading_window.geometry(f"+{x}+{y}")


        loading_label = tk.Label(self.loading_window, text="Loading, please wait...")
        loading_label.pack(expand=True, pady=20)
        
        # Step 3: Use after() to defer form loading after the UI updates
        self.root.after(100, self.load_form)

    def load_form(self):
        self.root.title("Add Patient")
        
        # Set the window size to the screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        frame_width = 1000
        frame_height = 700
        x = (screen_width // 2) - (frame_width // 2)
        y = (screen_height // 2) - (frame_height // 2)
        self.root.geometry(f"{frame_width}x{frame_height}+{x}+{y}")

        # Create a frame to hold everything inside a canvas for scrollability
        self.canvas = tk.Canvas(self.root, highlightthickness=0, bd=0)  # Remove focus/border indication
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Bind the mouse wheel to scroll the canvas
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows

        # Create an inner frame to hold all the form sections
        self.inner_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.inner_frame.bind("<Configure>", self.on_frame_configure)

        # Sections for form
        self.main_section = patient_form_main.MainSection(self.inner_frame)
        self.scholar_info_section = patient_form_scholar_info.ScholarInfo(self.inner_frame)
        self.evolution_section = patient_form_evolution.EvolutionHistorySection(self.inner_frame)
        self.prenatal_section = patient_form_prenatal.PrenatalSection(self.inner_frame)
        self.postnatal_section = patient_form_postnatal.PostnatalSection(self.inner_frame)
        self.health_section = patient_form_health.HealthHistory(self.inner_frame)
        self.treatments_section = patient_form_treatments.Treatments(self.inner_frame)
        self.scholar_history_section = patient_form_scholar_history.ScholarHistory(self.inner_frame)
        self.relationships_section = patient_form_relationships.PersonalRelationships(self.inner_frame)
        self.current_health_section = patient_form_health_history.HealthHistory(self.inner_frame)
        self.behavior_section = patient_form_behavior.BehaviorSection(self.inner_frame)

        # Submit button
        self.button_submit = tk.Button(self.root, text="Save New Patient", command=self.submit_form)
        self.button_submit.pack(pady=10)

        # Cancel button to close the window
        self.button_cancel = tk.Button(self.root, text="Cancel", command=self.close_window)
        self.button_cancel.pack(pady=10)

            # Step 2: Show the window once fully loaded
        self.root.update_idletasks()  # Make sure everything is built
        self.check_loading_complete()

    # Define the function to scroll the canvas
    def _on_mousewheel(self, event):
        if event.num == 5 or event.delta == -120:  # Scroll down
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:  # Scroll up
            self.canvas.yview_scroll(-1, "units")

    def on_frame_configure(self, event):
        # Update scroll region to the size of the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def submit_form(self):
        # load values from UI
        self.load_patient_values()
        create_new_patient(self.main_section_values, self.scholar_info_section_values, self.evo_section_values, self.prenatal_section_values, self.postnatal_section_values, self.development_section_values, self.health_section_values,
                            self.treatments_section_values, self.scholar_history_section_values, self.flunked_grades, self.academic_difficulty_section_values, self.relationships_section_values, self.current_health_section_values, self.behavior_section_values)

    def close_window(self):
        """Properly close the Toplevel window and re-enable the main window."""
        self.parent.grab_release()
        self.parent.attributes('-disabled', False)
        self.root.destroy()



    def load_patient_values(self):
        self.main_section_values = self.main_section.get_values()
        self.scholar_info_section_values = self.scholar_info_section.get_values()
        self.evo_section_values = self.evolution_section.get_values()
        self.prenatal_section_values = self.prenatal_section.get_values()
        self.postnatal_section_values = self.postnatal_section.get_postnatal_values()
        self.development_section_values = self.postnatal_section.get_development_values()
        self.health_section_values = self.health_section.get_illnesses_values()
        self.treatments_section_values = self.treatments_section.get_treatment_values()
        self.scholar_history_section_values = self.scholar_history_section.get_scholar_history_values()
        self.flunked_grades = self.scholar_history_section.get_flunked_grades()
        self.academic_difficulty_section_values = self.scholar_history_section.get_academic_difficulties_values()
        self.relationships_section_values = self.relationships_section.get_relationships_values()
        self.current_health_section_values = self.current_health_section.get_current_health_values()
        self.behavior_section_values = self.behavior_section.get_behavior_values()

    def check_loading_complete(self):
        if all([self.main_section, self.scholar_info_section, ...]):  # Check if sections are initialized
            self.loading_window.destroy()
            self.root.deiconify()
        else:
            self.root.after(50, self.check_loading_complete)


