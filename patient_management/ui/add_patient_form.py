import tkinter as tk
from tkinter import ttk

class AddPatientForm:
    def __init__(self, root, parent):
        self.root = root
        self.root.title("Add Patient")
        
        # Set the window size to the screen size
        screen_width = 900
        screen_height = 700
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.parent = parent

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
        self.create_main_section()
        self.create_scholar_history_section()
        self.create_evolution_history_section()
        self.create_prenatal_history_section()
        self.create_perinatal_history_section()
        self.create_postnatal_history_section()
        self.create_health_history_section()
        self.create_treatment_section()

        # Submit button
        self.button_submit = tk.Button(root, text="Submit", command=self.submit_form)
        self.button_submit.pack(pady=10)

        # Cancel button to close the window
        self.button_cancel = tk.Button(root, text="Cancel", command=self.close_window)
        self.button_cancel.pack(pady=10)

    # Define the function to scroll the canvas
    def _on_mousewheel(self, event):
        if event.num == 5 or event.delta == -120:  # Scroll down
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:  # Scroll up
            self.canvas.yview_scroll(-1, "units")

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

        self.create_toggle_button("Información General", main_frame)

        # Configure grid layout to stretch across the screen
        main_frame.grid_columnconfigure(0, weight=1)  # Column 0 (labels)
        main_frame.grid_columnconfigure(1, weight=2)  # Column 1 (entries)
        main_frame.grid_columnconfigure(2, weight=1)  # Column 0 (labels)
        main_frame.grid_columnconfigure(3, weight=2)  # Column 1 (entries)

        # Patient Name
        tk.Label(main_frame, text="Nombre con apellidos:").grid(row=0, column=0, sticky="w")
        self.entry_full_name = tk.Entry(main_frame)
        self.entry_full_name.grid(row=0, column=1)

        # Registry Number
        tk.Label(main_frame, text="Número de registro:").grid(row=0, column=2, sticky="w")
        self.entry_registry_number = tk.Entry(main_frame)
        self.entry_registry_number.grid(row=0, column=3)

        # Date of Birth
        tk.Label(main_frame, text="Fecha de nacimiento:").grid(row=1, column=0, sticky="w")
        self.entry_dob = tk.Entry(main_frame)
        self.entry_dob.grid(row=1, column=1)

        # Mother's Name
        tk.Label(main_frame, text="Nombre de la madre:").grid(row=1, column=2, sticky="w")
        self.entry_mother_name = tk.Entry(main_frame)
        self.entry_mother_name.grid(row=1, column=3)

        # Father's Name
        tk.Label(main_frame, text="Nombre del padre:").grid(row=2, column=0, sticky="w")
        self.entry_father_name = tk.Entry(main_frame)
        self.entry_father_name.grid(row=2, column=1)

        # Guardian Name
        tk.Label(main_frame, text="Nombre del encargado:").grid(row=2, column=2, sticky="w")
        self.entry_guardian_name = tk.Entry(main_frame)
        self.entry_guardian_name.grid(row=2, column=3)

        # Address
        tk.Label(main_frame, text="Dirección:").grid(row=3, column=0, sticky="w")
        self.entry_address = tk.Entry(main_frame)
        self.entry_address.grid(row=3, column=1)

        # Phone
        tk.Label(main_frame, text="Teléfono:").grid(row=3, column=2, sticky="w")
        self.entry_phone = tk.Entry(main_frame)
        self.entry_phone.grid(row=3, column=3)

        # Email
        tk.Label(main_frame, text="Email:").grid(row=4, column=0, sticky="w")
        self.entry_email = tk.Entry(main_frame)
        self.entry_email.grid(row=4, column=1)

    def create_prenatal_history_section(self):
        prenatal_frame = tk.LabelFrame(self.inner_frame, text="Historial Prenatal", padx=10, pady=10)
        prenatal_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Historial Prenatal", prenatal_frame)
        self.otras_enfermedades_var = tk.BooleanVar()

        self.prenatal_vars = {
            "Normal": tk.BooleanVar(),
            "Alta presión": tk.BooleanVar(),
            "Diabetes": tk.BooleanVar(),
            "Caídas": tk.BooleanVar(),
            "Sangrado": tk.BooleanVar(),
            "Accidentes": tk.BooleanVar(),
            "Uso de drogas, alcohol": tk.BooleanVar(),
            "Vómitos frecuentes": tk.BooleanVar(),
            "Uso de Medicamentos": tk.BooleanVar(),
            "Otras enfermedades:": self.otras_enfermedades_var,
        }

        row = 0
        column = 0
        for label, var in self.prenatal_vars.items():
            if label == "Otras enfermedades:":
                tk.Checkbutton(prenatal_frame, text=label, variable=var, command=self.on_check_otras_enfermedades).grid(row=row, column=column, sticky="w", padx=5, pady=5)
            else:
                tk.Checkbutton(prenatal_frame, text=label, variable=var).grid(row=row, column=column, sticky="w", padx=5, pady=5)
            if column == 2:
                column = 0
                row += 1
            else:
                column += 1

        # Other Illnesses (Entry field)
        self.entry_other_illnesses = tk.Entry(prenatal_frame)
        self.entry_other_illnesses.grid(row=row, column=1, sticky="w", padx=5, pady=5)
        self.entry_other_illnesses.config(state="disabled")

        # Mother's Emotional State (Entry field)
        tk.Label(prenatal_frame, text="Estado emocional de la madre:").grid(row=row + 1, column=0, sticky="w")
        self.entry_mother_emotional_state = tk.Entry(prenatal_frame)
        self.entry_mother_emotional_state.grid(row=row + 1, column=1, sticky="w", padx=5, pady=5)

    def create_perinatal_history_section(self):
        perinatal_frame = tk.LabelFrame(self.inner_frame, text="Historial perinatal", padx=10, pady=10)
        perinatal_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Historial perinatal", perinatal_frame)

        self.parto_natural_cb = tk.Checkbutton(perinatal_frame, text="Parto Natural", variable=tk.BooleanVar).grid(row=0, column=0, sticky="w")
        self.parto_cesarea_cb = tk.Checkbutton(perinatal_frame, text="Parto Cesárea", variable=tk.BooleanVar).grid(row=0, column=1, sticky="w")
        self.parto_prematuro_cb = tk.Checkbutton(perinatal_frame, text="Parto prematuro", variable=tk.BooleanVar).grid(row=0, column=2, sticky="w")
        self.complicaciones_var = tk.BooleanVar()
        self.parto_complications_cb = tk.Checkbutton(perinatal_frame, text="Complicaciones durante el parto:", variable=self.complicaciones_var, command=self.on_check_complications).grid(row=1, column=0, sticky="w")

        self.entry_complications = tk.Entry(perinatal_frame, state="disabled")
        self.entry_complications.grid(row=1, column=1, sticky="w")

    def create_postnatal_history_section(self):
        postnatal_frame = tk.LabelFrame(self.inner_frame, text="Historial Postnatal", padx=10, pady=10)
        postnatal_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Historial Postnatal", postnatal_frame)


        self.normal_var = tk.BooleanVar()
        self.cianosis_var = tk.BooleanVar()
        self.meningitis_var = tk.BooleanVar()
        self.ictericia_var = tk.BooleanVar()
        self.convulciones_var = tk.BooleanVar()
        self.incubadora_var = tk.BooleanVar()
        self.otras_condiciones_var = tk.BooleanVar()
        self.postnatal_vars = {
            "Normal": self.normal_var,
            "Cianosis": self.cianosis_var,
            "Meningitis": self.meningitis_var,
            "Ictericia": self.ictericia_var,
            "Convulsiones": self.convulciones_var,
            "Incubadora": self.incubadora_var,
            "Otras Condiciones:": self.otras_condiciones_var,
        }

        row = 0
        column = 0
        for label, var in self.postnatal_vars.items():
            if(label=="Incubadora"):
                tk.Label(postnatal_frame, text="Tiempo:").grid(row=row, column=column+1, sticky="w")
                self.entry_incubator_time = tk.Entry(postnatal_frame)
                self.entry_incubator_time.grid(row=row, column=column+2)
                self.entry_incubator_time.config(state="disabled")
                tk.Checkbutton(postnatal_frame, text=label, variable=var, command=self.on_check_incubadora).grid(row=row, column=column, sticky="w")
            elif label=="Otras Condiciones:":
                tk.Checkbutton(postnatal_frame, text=label, variable=var, command=self.on_check_otras_condiciones).grid(row=row, column=column, sticky="w")
            else:
                tk.Checkbutton(postnatal_frame, text=label, variable=var).grid(row=row, column=column, sticky="w")
            if column == 2:
                column = 0
                row += 1
            else:
                column += 1

        self.entry_other_conditions = tk.Entry(postnatal_frame)
        self.entry_other_conditions.grid(row=row, column=1)
        self.entry_other_conditions.config(state="disabled")

        # Weight at birth
        tk.Label(postnatal_frame, text="Peso al nacer:").grid(row=row + 2, column=0, sticky="w")
        self.entry_weight_at_birth = tk.Entry(postnatal_frame)
        self.entry_weight_at_birth.grid(row=row + 2, column=1)

        # Size at birth
        tk.Label(postnatal_frame, text="Tamaño al nacer:").grid(row=row + 3, column=0, sticky="w")
        self.entry_size_at_birth = tk.Entry(postnatal_frame)
        self.entry_size_at_birth.grid(row=row + 3, column=1)

        tk.Label(postnatal_frame, text="Desarrollo").grid(row=row + 4, column=0, sticky="w")

        # Psycholinguistic Development
        tk.Label(postnatal_frame, text="Desarrollo psicolinguistico:").grid(row=row + 5, column=0, sticky="w")
        self.psycholinguistic_dev = ttk.Combobox(postnatal_frame, values=["Normal", "Rápido", "Lento", "Dificultad en:"], state="readonly")
        self.psycholinguistic_dev.grid(row=row + 5, column=1)
        self.psycholinguistic_dev.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_psycholinguistic_difficulties = tk.Entry(postnatal_frame, state = "disabled")
        self.entry_psycholinguistic_difficulties.grid(row=row + 5, column=2)
        self.psycholinguistic_dev.bind("<<ComboboxSelected>>", self.on_psycholinguistic_difficulty_combobox_select)

        # Psychomotor Development
        tk.Label(postnatal_frame, text="Desarrollo psicomotor:").grid(row=row + 7, column=0, sticky="w")
        self.psychomotor_dev = ttk.Combobox(postnatal_frame, values=["Normal", "Rápido", "Lento", "Dificultad en:"], state="readonly")
        self.psychomotor_dev.grid(row=row + 7, column=1)
        self.psychomotor_dev.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_psychomotor_difficulties = tk.Entry(postnatal_frame, state="disabled")
        self.entry_psychomotor_difficulties.grid(row=row + 7, column=2)
        self.psychomotor_dev.bind("<<ComboboxSelected>>", self.on_psychomotor_difficulty_combobox_select)

        # Activity level
        tk.Label(postnatal_frame, text="Nivel de actividad").grid(row=row + 9, column=0, sticky="w")
        self.activity_level = ttk.Combobox(postnatal_frame, values=["Tranquilo", "Inquieto", "Hiperactivo", "Hipoactivo"], state="readonly")
        self.activity_level.grid(row=row + 9, column=1)
        self.activity_level.bind("<MouseWheel>", self.empty_scroll_command)

        # Development milestones
        tk.Label(postnatal_frame, text="Especifique a qué edad llevó a cabo las siguientes actividades:").grid(row=row+10, column=0, columnspan=2, sticky="nsew")
        tk.Label(postnatal_frame, text="Clave: (L) lento    (AN) aparentemente normal    (NL) no logrado").grid(row=row+11, column=0, columnspan=2, sticky="nsew")
         # List of milestones
        milestones = [
            "Virarse", "Sentarse", "Gatear", "Caminar", "Pararse con soporte",
            "Pararse sin soporte", "Brincar en un pie", "Brincar en ambos pies", "Saltar", "Jugar"
        ]

        # Combobox options
        options = ["L", "AP", "NL"]

        # Loop through the milestones and create corresponding labels and comboboxes
        self.milestone_vars = {}  # Dictionary to store the Combobox variables for later use
        milestones_column = 0
        for milestone in milestones:
            tk.Label(postnatal_frame, text=milestone + ":").grid(row=row+12, column=milestones_column, sticky="w")
            
            # Create a Combobox for each milestone
            combobox = ttk.Combobox(postnatal_frame, values=options, state="readonly")
            combobox.grid(row=row+12, column=milestones_column+1, padx=5, pady=2)
            combobox.bind("<MouseWheel>", self.empty_scroll_command)
            
            # Store the combobox in the dictionary with the milestone as the key
            self.milestone_vars[milestone] = combobox
            if(milestones_column == 0):
                milestones_column =2
            else:
                milestones_column = 0
                row += 1

    def create_scholar_history_section(self):
        scholar_frame = tk.LabelFrame(self.inner_frame, text="Historial Escolar", padx=10, pady=10)
        scholar_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Historial Escolar", scholar_frame)

        # School
        tk.Label(scholar_frame, text="Escuela:").grid(row=0, column=0, sticky="w")
        self.entry_school = tk.Entry(scholar_frame)
        self.entry_school.grid(row=0, column=1)

        # Education region
        tk.Label(scholar_frame, text="Región educativa:").grid(row=0, column=2, sticky="w")
        self.entry_education_region = tk.Entry(scholar_frame)
        self.entry_education_region.grid(row=0, column=3)

        # Municipality
        tk.Label(scholar_frame, text="Municipio:").grid(row=1, column=0, sticky="w")
        self.entry_municipality = tk.Entry(scholar_frame)
        self.entry_municipality.grid(row=1, column=1)

        # District
        tk.Label(scholar_frame, text="Distrito:").grid(row=1, column=2, sticky="w")
        self.entry_district = tk.Entry(scholar_frame)
        self.entry_district.grid(row=1, column=3)

        # Grade/group
        tk.Label(scholar_frame, text="Grado/Grupo:").grid(row=2, column=0, sticky="w")
        self.entry_grade_group = tk.Entry(scholar_frame)
        self.entry_grade_group.grid(row=2, column=1)

        # Post
        tk.Label(scholar_frame, text="Puesto:").grid(row=2, column=2, sticky="w")
        self.entry_post = tk.Entry(scholar_frame)
        self.entry_post.grid(row=2, column=3)

    def create_evolution_history_section(self):
        relationship_frame = tk.LabelFrame(self.inner_frame, text="Historial del desarrollo evolutivo", padx=10, pady=10)
        relationship_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Historial del desarrollo evolutivo", relationship_frame)
        # History Origin - Dropdown selection
        tk.Label(relationship_frame, text="Historial del desarrollo evolutivo surge de:").grid(row=0, column=0, sticky="w")
        self.history_origin = ttk.Combobox(relationship_frame, values=["entrevista", "lectura de expediente"], state="readonly")
        self.history_origin.grid(row=0, column=1)
        self.history_origin.bind("<MouseWheel>", self.empty_scroll_command)

        # People living at home
        tk.Label(relationship_frame, text="Vive con:").grid(row=1, column=0, sticky="w")
        self.mama_var = tk.BooleanVar()
        self.papa_var = tk.BooleanVar()
        self.hermanos_var = tk.BooleanVar()
        self.abuelos_var = tk.BooleanVar()
        self.otros_var = tk.BooleanVar()

        family_members = {
            "Mamá" : self.mama_var,
            "Papá" : self.papa_var,
            "Hermanos" : self.hermanos_var,
            "Abuelos" : self.abuelos_var,
            "Otros:" : self.otros_var,}
        fam_member_col = 0
        for family_member, var in family_members.items():
            if family_member == "Otros:":
                tk.Checkbutton(relationship_frame, text=family_member, variable=var, command=self.on_otros_check).grid(row=2, column=fam_member_col, sticky="w")
            else:
                tk.Checkbutton(relationship_frame, text=family_member, variable=var).grid(row=2, column=fam_member_col, sticky="w")
            fam_member_col += 1
        self.entry_people_at_home = tk.Entry(relationship_frame)
        self.entry_people_at_home.grid(row=2, column=5)
        self.entry_people_at_home.config(state="disabled")

        # Problems at home
        self.problems_at_home_var = tk.BooleanVar()
        tk.Checkbutton(relationship_frame, text="Problemas en el hogar:", variable=self.problems_at_home_var, command=self.on_check_problems_at_home).grid(row=3, column=0, sticky="w")
        self.entry_problems_at_home = tk.Entry(relationship_frame)
        self.entry_problems_at_home.grid(row=3, column=1)
        self.entry_problems_at_home.config(state="disabled")

    def create_health_history_section(self):
        health_frame = tk.LabelFrame(self.inner_frame, text="Enfermedades", padx=10, pady=10)
        health_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Enfermedades", health_frame)

        #Illnesses
        self.asma_bronquial_var = tk.BooleanVar()
        self.pulmonia_var = tk.BooleanVar()
        self.fiebres_var = tk.BooleanVar()
        self.convulsiones_enfermedades_var = tk.BooleanVar()
        self.cirugias_var = tk.BooleanVar()
        self.diabetes_var = tk.BooleanVar()
        self.other_illnesses_var = tk.BooleanVar()
        illneses = {
            "Asma bronquial" : self.asma_bronquial_var,
            "Pulmonía" : self.pulmonia_var,
            "Fiebres muy altas" : self.fiebres_var,
            "Convulsiones" : self.convulsiones_enfermedades_var,
            "Cirugías" : self.cirugias_var, 
            "Diabetes" : self.diabetes_var,
            "Otras condiciones:" : self.other_illnesses_var,
        }
        row = 0
        health_col=0
        for illness, var in illneses.items():
            if illness == "Otras condiciones:":
                tk.Checkbutton(health_frame, text=illness, variable=var, command=self.on_check_other_illnesses).grid(row=row, column=health_col, sticky="w")
            else:
                tk.Checkbutton(health_frame, text=illness, variable=var).grid(row=row, column=health_col, sticky="w")

            if health_col < 2:
                health_col += 1
            else:
                health_col=0
                row+=1

        self.entry_other_illnesses = tk.Entry(health_frame)
        self.entry_other_illnesses.grid(row=2, column=1)
        self.entry_other_illnesses.config(state="disabled")
    
    def create_treatment_section(self):
        treatment_frame = tk.LabelFrame(self.inner_frame, text="Tratamiento:", padx=10, pady=10)
        treatment_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Tratamiento", treatment_frame)

        #Tratamientos
        tk.Label(treatment_frame, text="Disciplina").grid(row=0, column=0, sticky="w")
        tk.Label(treatment_frame, text="Frecuencia").grid(row=0, column=1, sticky="w")
        tk.Label(treatment_frame, text="Duración").grid(row=0, column=2, sticky="w")
        tk.Label(treatment_frame, text="Modalidad").grid(row=0, column=3, sticky="w")
        tk.Label(treatment_frame, text="Inicio de Servicio").grid(row=0, column=4, sticky="w")
        tk.Label(treatment_frame, text="Estatus").grid(row=0, column=5, sticky="w")

        tk.Label(treatment_frame, text="Habla-Lenguaje").grid(row=1, column=0, sticky="w")
        self.habla_frequency_combo = ttk.Combobox(treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.habla_frequency_combo.grid(row=1, column=1)
        self.habla_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.habla_duration_combo = ttk.Combobox(treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.habla_duration_combo.grid(row=1, column=2)
        self.habla_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.habla_modalidad_combo = ttk.Combobox(treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.habla_modalidad_combo.grid(row=1, column=2)
        self.habla_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_habla = ttk.Entry(treatment_frame).grid(row=1, column=3)
        self.habla_status_combo = ttk.Combobox(treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.habla_status_combo.grid(row=1, column=4)
        self.habla_status_combo.bind("<MouseWheel>", self.empty_scroll_command)

    def create_toggle_button(self, text, frame):
        toggle_button = tk.Button(self.inner_frame, text=f"Toggle {text}", command=lambda: self.toggle_section(frame), relief=tk.FLAT)
        toggle_button.pack(pady=2, anchor="e")

    def submit_form(self):
        # Collect and process form data
        print("Form submitted")

    def close_window(self):
        self.root.destroy()
    
    def empty_scroll_command(self, event):
        return "break"
    
    def on_psycholinguistic_difficulty_combobox_select(self, event):
        selected_value = self.psycholinguistic_dev.get()
        if selected_value == "Dificultad en:":
            # Enable the entry field if "Dificultad en" is selected
            self.entry_psycholinguistic_difficulties.config(state="normal")
        else:
            # Disable the entry field for other selections
            self.entry_psycholinguistic_difficulties.delete(0, tk.END) 
            self.entry_psycholinguistic_difficulties.config(state="disabled")   

    def on_psychomotor_difficulty_combobox_select(self, event):
        selected_value = self.psychomotor_dev.get()
        if selected_value == "Dificultad en:":
            # Enable the entry field if "Dificultad en" is selected
            self.entry_psychomotor_difficulties.config(state="normal")
        else:
            # Disable the entry field for other selections
            self.entry_psychomotor_difficulties.delete(0, tk.END)   
            self.entry_psychomotor_difficulties.config(state="disabled")

    def on_check_complications(self):
        if self.complicaciones_var.get():
            self.entry_complications.config(state="normal")
        else:
            self.entry_complications.delete(0, tk.END)
            self.entry_complications.config(state="disabled")
    def on_otros_check(self):
        if self.otros_var.get():
            self.entry_people_at_home.config(state="normal")
        else:
            self.entry_people_at_home.delete(0, tk.END)
            self.entry_people_at_home.config(state="disabled")

    def on_check_otras_enfermedades(self):
        if self.otras_enfermedades_var.get():
            self.entry_other_illnesses.config(state="normal")
        else:
            self.entry_other_illnesses.delete(0, tk.END)
            self.entry_other_illnesses.config(state="disabled")

    def on_check_problems_at_home(self):
        if self.problems_at_home_var.get():
            self.entry_problems_at_home.config(state="normal")
        else:
            self.entry_problems_at_home.delete(0, tk.END)
            self.entry_problems_at_home.config(state="disabled")

    def on_check_incubadora(self):
        if self.incubadora_var.get():
            self.entry_incubator_time.config(state="normal")
        else:
            self.entry_incubator_time.delete(0, tk.END)
            self.entry_incubator_time.config(state="disabled")

    def on_check_otras_condiciones(self):
        if self.otras_condiciones_var.get():
            self.entry_other_conditions.config(state="normal")
        else:
            self.entry_other_conditions.delete(0, tk.END)
            self.entry_other_conditions.config(state="disabled")
    
    def on_check_other_illnesses(self):
        if self.other_illnesses_var.get():
            self.entry_other_illnesses.config(state="normal")
        else:
            self.entry_other_illnesses.delete(0, tk.END)
            self.entry_other_illnesses.config(state="disabled")
     

# For testing the form
if __name__ == "__main__":
    root = tk.Tk()
    app = AddPatientForm(root, parent=None)
    root.mainloop()