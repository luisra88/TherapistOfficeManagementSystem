import tkinter as tk
from tkinter import ttk

class AddPatientForm:
    def __init__(self, root, parent):
        self.root = root
        self.root.title("Add Patient")
        
        # Set the window size to the screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.parent = parent

        # Create a frame to hold everything inside a canvas for scrollability
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create an inner frame to hold all the form sections
        self.inner_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.inner_frame.bind("<Configure>", self.on_frame_configure)

        # Sections for form
        self.create_main_section()
        self.create_prenatal_history_section()
        self.create_perinatal_history_section()
        self.create_postnatal_history_section()
        self.create_scholar_history_section()
        self.create_relationship_history_section()
        self.create_health_history_section()
        self.create_behavior_history_section()

        # Submit button
        self.button_submit = tk.Button(root, text="Submit", command=self.submit_form)
        self.button_submit.pack(pady=10)

        # Cancel button to close the window
        self.button_cancel = tk.Button(root, text="Cancel", command=self.close_window)
        self.button_cancel.pack(pady=10)

    def on_frame_configure(self, event):
        # Update scroll region to the size of the inner frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def toggle_section(self, section_frame):
        if section_frame.winfo_viewable():
            section_frame.pack_forget()
        else:
            section_frame.pack(fill="x", padx=10, pady=5)

    def create_main_section(self):
        main_frame = tk.LabelFrame(self.inner_frame, text="Main Section", padx=10, pady=10)
        main_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Main Section", main_frame)

        # Patient Name
        tk.Label(main_frame, text="Full Name:").grid(row=0, column=0, sticky="w")
        self.entry_full_name = tk.Entry(main_frame)
        self.entry_full_name.grid(row=0, column=1)

        # Registry Number
        tk.Label(main_frame, text="Registry Number:").grid(row=1, column=0, sticky="w")
        self.entry_registry_number = tk.Entry(main_frame)
        self.entry_registry_number.grid(row=1, column=1)

        # Date of Birth
        tk.Label(main_frame, text="Date of Birth:").grid(row=2, column=0, sticky="w")
        self.entry_dob = tk.Entry(main_frame)
        self.entry_dob.grid(row=2, column=1)

        # Mother's Name
        tk.Label(main_frame, text="Mother's Name:").grid(row=3, column=0, sticky="w")
        self.entry_mother_name = tk.Entry(main_frame)
        self.entry_mother_name.grid(row=3, column=1)

        # Father's Name
        tk.Label(main_frame, text="Father's Name:").grid(row=4, column=0, sticky="w")
        self.entry_father_name = tk.Entry(main_frame)
        self.entry_father_name.grid(row=4, column=1)

        # Guardian Name
        tk.Label(main_frame, text="Guardian's Name:").grid(row=5, column=0, sticky="w")
        self.entry_guardian_name = tk.Entry(main_frame)
        self.entry_guardian_name.grid(row=5, column=1)

        # Address
        tk.Label(main_frame, text="Address:").grid(row=6, column=0, sticky="w")
        self.entry_address = tk.Entry(main_frame)
        self.entry_address.grid(row=6, column=1)

        # Phone
        tk.Label(main_frame, text="Phone:").grid(row=7, column=0, sticky="w")
        self.entry_phone = tk.Entry(main_frame)
        self.entry_phone.grid(row=7, column=1)

        # Email
        tk.Label(main_frame, text="Email:").grid(row=8, column=0, sticky="w")
        self.entry_email = tk.Entry(main_frame)
        self.entry_email.grid(row=8, column=1)

        # History Origin - Dropdown selection
        tk.Label(main_frame, text="History Origin:").grid(row=9, column=0, sticky="w")
        self.history_origin = ttk.Combobox(main_frame, values=["Interview", "File"])
        self.history_origin.grid(row=9, column=1)

    def create_prenatal_history_section(self):
        prenatal_frame = tk.LabelFrame(self.inner_frame, text="Prenatal History", padx=10, pady=10)
        prenatal_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Prenatal History", prenatal_frame)

        self.prenatal_vars = {
            "Normal": tk.BooleanVar(),
            "High Pressure": tk.BooleanVar(),
            "Diabetes": tk.BooleanVar(),
            "Falls": tk.BooleanVar(),
            "Bleeds": tk.BooleanVar(),
            "Accidents": tk.BooleanVar(),
            "Drug/Alcohol Use": tk.BooleanVar(),
            "Frequent Vomits": tk.BooleanVar(),
            "Use of Medicines": tk.BooleanVar(),
            "Other Illnesses": tk.BooleanVar(),
            "Mother's Emotional State": tk.BooleanVar(),
        }

        row = 0
        for label, var in self.prenatal_vars.items():
            tk.Checkbutton(prenatal_frame, text=label, variable=var).grid(row=row, column=0, sticky="w")
            row += 1

        # Other Illnesses (comment field)
        self.entry_other_illnesses = tk.Entry(prenatal_frame)
        self.entry_other_illnesses.grid(row=row, column=1)
        self.entry_other_illnesses.grid_remove()

        self.entry_mother_emotional_state = tk.Entry(prenatal_frame)
        self.entry_mother_emotional_state.grid(row=row + 1, column=1)
        self.entry_mother_emotional_state.grid_remove()

    def create_perinatal_history_section(self):
        perinatal_frame = tk.LabelFrame(self.inner_frame, text="Perinatal History", padx=10, pady=10)
        perinatal_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Perinatal History", perinatal_frame)

        self.perinatal_vars = {
            "Natural Birth": tk.BooleanVar(),
            "C Section": tk.BooleanVar(),
            "Premature Birth": tk.BooleanVar(),
            "Complications During Birth": tk.BooleanVar(),
        }

        row = 0
        for label, var in self.perinatal_vars.items():
            tk.Checkbutton(perinatal_frame, text=label, variable=var).grid(row=row, column=0, sticky="w")
            row += 1

        self.entry_complications = tk.Entry(perinatal_frame)
        self.entry_complications.grid(row=row, column=1)
        self.entry_complications.grid_remove()

    def create_postnatal_history_section(self):
        postnatal_frame = tk.LabelFrame(self.inner_frame, text="Postnatal History", padx=10, pady=10)
        postnatal_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Postnatal History", postnatal_frame)

        self.postnatal_vars = {
            "Normal": tk.BooleanVar(),
            "Cianosis": tk.BooleanVar(),
            "Meningitis": tk.BooleanVar(),
            "Ictericia": tk.BooleanVar(),
            "Seizures": tk.BooleanVar(),
            "Incubator": tk.BooleanVar(),
            "Other Conditions": tk.BooleanVar(),
        }

        row = 0
        for label, var in self.postnatal_vars.items():
            tk.Checkbutton(postnatal_frame, text=label, variable=var).grid(row=row, column=0, sticky="w")
            row += 1

        self.entry_incubator_time = tk.Entry(postnatal_frame)
        self.entry_incubator_time.grid(row=row, column=1)
        self.entry_incubator_time.grid_remove()

        self.entry_other_conditions = tk.Entry(postnatal_frame)
        self.entry_other_conditions.grid(row=row + 1, column=1)
        self.entry_other_conditions.grid_remove()

        # Weight at birth
        tk.Label(postnatal_frame, text="Weight at Birth:").grid(row=row + 2, column=0, sticky="w")
        self.entry_weight_at_birth = tk.Entry(postnatal_frame)
        self.entry_weight_at_birth.grid(row=row + 2, column=1)

        # Size at birth
        tk.Label(postnatal_frame, text="Size at Birth:").grid(row=row + 3, column=0, sticky="w")
        self.entry_size_at_birth = tk.Entry(postnatal_frame)
        self.entry_size_at_birth.grid(row=row + 3, column=1)

        # Psycholinguistic Development
        tk.Label(postnatal_frame, text="Psycholinguistic Development:").grid(row=row + 4, column=0, sticky="w")
        self.psycholinguistic_dev = ttk.Combobox(postnatal_frame, values=["Normal", "Fast", "Slow", "Difficulties"])
        self.psycholinguistic_dev.grid(row=row + 4, column=1)

        self.entry_psycholinguistic_difficulties = tk.Entry(postnatal_frame)
        self.entry_psycholinguistic_difficulties.grid(row=row + 5, column=1)
        self.entry_psycholinguistic_difficulties.grid_remove()

        # Psychomotor Development
        tk.Label(postnatal_frame, text="Psychomotor Development:").grid(row=row + 6, column=0, sticky="w")
        self.psychomotor_dev = ttk.Combobox(postnatal_frame, values=["Normal", "Fast", "Slow", "Difficulties"])
        self.psychomotor_dev.grid(row=row + 6, column=1)

        self.entry_psychomotor_difficulties = tk.Entry(postnatal_frame)
        self.entry_psychomotor_difficulties.grid(row=row + 7, column=1)
        self.entry_psychomotor_difficulties.grid_remove()

    def create_scholar_history_section(self):
        scholar_frame = tk.LabelFrame(self.inner_frame, text="Scholar History", padx=10, pady=10)
        scholar_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Scholar History", scholar_frame)

        # School
        tk.Label(scholar_frame, text="School:").grid(row=0, column=0, sticky="w")
        self.entry_school = tk.Entry(scholar_frame)
        self.entry_school.grid(row=0, column=1)

        # Education region
        tk.Label(scholar_frame, text="Education Region:").grid(row=1, column=0, sticky="w")
        self.entry_education_region = tk.Entry(scholar_frame)
        self.entry_education_region.grid(row=1, column=1)

        # Municipality
        tk.Label(scholar_frame, text="Municipality:").grid(row=2, column=0, sticky="w")
        self.entry_municipality = tk.Entry(scholar_frame)
        self.entry_municipality.grid(row=2, column=1)

        # District
        tk.Label(scholar_frame, text="District:").grid(row=3, column=0, sticky="w")
        self.entry_district = tk.Entry(scholar_frame)
        self.entry_district.grid(row=3, column=1)

        # Grade/group
        tk.Label(scholar_frame, text="Grade/Group:").grid(row=4, column=0, sticky="w")
        self.entry_grade_group = tk.Entry(scholar_frame)
        self.entry_grade_group.grid(row=4, column=1)

        # Post
        tk.Label(scholar_frame, text="Post:").grid(row=5, column=0, sticky="w")
        self.entry_post = tk.Entry(scholar_frame)
        self.entry_post.grid(row=5, column=1)

    def create_relationship_history_section(self):
        relationship_frame = tk.LabelFrame(self.inner_frame, text="Relationship History", padx=10, pady=10)
        relationship_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Relationship History", relationship_frame)

        # People living at home
        tk.Label(relationship_frame, text="People Living at Home:").grid(row=0, column=0, sticky="w")
        self.entry_people_at_home = tk.Entry(relationship_frame)
        self.entry_people_at_home.grid(row=0, column=1)

        # Problems at home
        tk.Label(relationship_frame, text="Problems at Home:").grid(row=1, column=0, sticky="w")
        self.entry_problems_at_home = tk.Entry(relationship_frame)
        self.entry_problems_at_home.grid(row=1, column=1)

    def create_health_history_section(self):
        health_frame = tk.LabelFrame(self.inner_frame, text="Health History", padx=10, pady=10)
        health_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Health History", health_frame)

        # Current illnesses
        tk.Label(health_frame, text="Current Illnesses:").grid(row=0, column=0, sticky="w")
        self.entry_current_illnesses = tk.Entry(health_frame)
        self.entry_current_illnesses.grid(row=0, column=1)

    def create_behavior_history_section(self):
        behavior_frame = tk.LabelFrame(self.inner_frame, text="Behavior History", padx=10, pady=10)
        behavior_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Behavior History", behavior_frame)

        # Activity level
        tk.Label(behavior_frame, text="Activity Level:").grid(row=0, column=0, sticky="w")
        self.activity_level = ttk.Combobox(behavior_frame, values=["Low", "Medium", "High"])
        self.activity_level.grid(row=0, column=1)

        # Development milestones
        tk.Label(behavior_frame, text="Milestones:").grid(row=1, column=0, sticky="w")
        self.entry_milestones = tk.Entry(behavior_frame)
        self.entry_milestones.grid(row=1, column=1)

    def create_toggle_button(self, text, frame):
        toggle_button = tk.Button(self.inner_frame, text=f"Toggle {text}", command=lambda: self.toggle_section(frame), relief=tk.FLAT)
        toggle_button.pack(pady=2, anchor="e")

    def submit_form(self):
        # Collect and process form data
        print("Form submitted")

    def close_window(self):
        self.root.destroy()

# For testing the form
if __name__ == "__main__":
    root = tk.Tk()
    app = AddPatientForm(root, parent=None)
    root.mainloop()