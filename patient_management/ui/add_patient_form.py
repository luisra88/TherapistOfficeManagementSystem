import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class AddPatientForm:
    def __init__(self, root, parent):
        self.root = root
        self.root.title("Add Patient")
        
        # Set the window size to the screen size
        screen_width = 1000
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
        self.create_scholar_info_section()
        self.create_evolution_history_section()
        self.create_prenatal_history_section()
        self.create_perinatal_history_section()
        self.create_postnatal_history_section()
        self.create_health_history_section()
        self.create_treatment_section()
        self.create_historial_escolar_section()
        self.create_relaciones_interpersonales_section()
        self.create_salud_actual_section()
        self.create_conducta_section()

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

    def create_scholar_info_section(self):
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
        tk.Label(treatment_frame, text="Fecha de Inicio").grid(row=0, column=4, sticky="w")
        tk.Label(treatment_frame, text="Estatus").grid(row=0, column=5, sticky="w")

        self.habla_var = tk.BooleanVar()
        tk.Checkbutton(treatment_frame, text="Habla-Lenguaje", variable=self.habla_var, command=self.on_check_habla).grid(row=1, column=0, sticky="w")
        self.habla_frequency_combo = ttk.Combobox(treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.habla_frequency_combo.grid(row=1, column=1)
        self.habla_frequency_combo.config(state="disabled")
        self.habla_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.habla_duration_combo = ttk.Combobox(treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.habla_duration_combo.grid(row=1, column=2)
        self.habla_duration_combo.config(state="disabled")
        self.habla_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.habla_modalidad_combo = ttk.Combobox(treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.habla_modalidad_combo.grid(row=1, column=3)
        self.habla_modalidad_combo.config(state="disabled")
        self.habla_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_habla = ttk.Entry(treatment_frame)
        self.entry_habla.grid(row=1, column=4)
        self.entry_habla.config(state="disabled")
        self.habla_status_combo = ttk.Combobox(treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.habla_status_combo.grid(row=1, column=5)
        self.habla_status_combo.config(state="disabled")
        self.habla_status_combo.bind("<MouseWheel>", self.empty_scroll_command)

        self.ocupacional_var = tk.BooleanVar()
        tk.Checkbutton(treatment_frame, text="Ocupacional", variable=self.ocupacional_var, command=self.on_check_ocupacional).grid(row=2, column=0, sticky="w")
        self.ocupacional_frequency_combo = ttk.Combobox(treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.ocupacional_frequency_combo.grid(row=2, column=1)
        self.ocupacional_frequency_combo.config(state="disabled")
        self.ocupacional_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.ocupacional_duration_combo = ttk.Combobox(treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.ocupacional_duration_combo.grid(row=2, column=2)
        self.ocupacional_duration_combo.config(state="disabled")
        self.ocupacional_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.ocupacional_modalidad_combo = ttk.Combobox(treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.ocupacional_modalidad_combo.grid(row=2, column=3)
        self.ocupacional_modalidad_combo.config(state="disabled")
        self.ocupacional_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_ocupacional = ttk.Entry(treatment_frame)
        self.entry_ocupacional.grid(row=2, column=4)
        self.entry_ocupacional.config(state="disabled")
        self.ocupacional_status_combo = ttk.Combobox(treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.ocupacional_status_combo.grid(row=2, column=5)
        self.ocupacional_status_combo.config(state="disabled")
        self.ocupacional_status_combo.bind("<MouseWheel>", self.empty_scroll_command)

        self.psicologica_var = tk.BooleanVar()
        tk.Checkbutton(treatment_frame, text="Psicológica", variable=self.psicologica_var, command=self.on_check_psicologica).grid(row=3, column=0, sticky="w")
        self.psicologica_frequency_combo = ttk.Combobox(treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.psicologica_frequency_combo.grid(row=3, column=1)
        self.psicologica_frequency_combo.config(state="disabled")
        self.psicologica_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.psicologica_duration_combo = ttk.Combobox(treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.psicologica_duration_combo.grid(row=3, column=2)
        self.psicologica_duration_combo.config(state="disabled")
        self.psicologica_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.psicologica_modalidad_combo = ttk.Combobox(treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.psicologica_modalidad_combo.grid(row=3, column=3)
        self.psicologica_modalidad_combo.config(state="disabled")
        self.psicologica_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_psicologica = ttk.Entry(treatment_frame)
        self.entry_psicologica.grid(row=3, column=4)
        self.entry_psicologica.config(state="disabled")
        self.psicologica_status_combo = ttk.Combobox(treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.psicologica_status_combo.grid(row=3, column=5)
        self.psicologica_status_combo.config(state="disabled")
        self.psicologica_status_combo.bind("<MouseWheel>", self.empty_scroll_command)

        self.fisica_var = tk.BooleanVar()
        tk.Checkbutton(treatment_frame, text="Física", variable=self.fisica_var, command=self.on_check_fisica).grid(row=4, column=0, sticky="w")
        self.fisica_frequency_combo = ttk.Combobox(treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.fisica_frequency_combo.grid(row=4, column=1)
        self.fisica_frequency_combo.config(state="disabled")
        self.fisica_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.fisica_duration_combo = ttk.Combobox(treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.fisica_duration_combo.grid(row=4, column=2)
        self.fisica_duration_combo.config(state="disabled")
        self.fisica_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.fisica_modalidad_combo = ttk.Combobox(treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.fisica_modalidad_combo.grid(row=4, column=3)
        self.fisica_modalidad_combo.config(state="disabled")
        self.fisica_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_fisica = ttk.Entry(treatment_frame)
        self.entry_fisica.grid(row=4, column=4)
        self.entry_fisica.config(state="disabled")
        self.fisica_status_combo = ttk.Combobox(treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.fisica_status_combo.grid(row=4, column=5)
        self.fisica_status_combo.config(state="disabled")
        self.fisica_status_combo.bind("<MouseWheel>", self.empty_scroll_command)

        self.psicquiatrica_var = tk.BooleanVar()
        tk.Checkbutton(treatment_frame, text="Psicquiátrica", variable=self.psicquiatrica_var, command=self.on_check_psicquiatrica).grid(row=5, column=0, sticky="w")
        self.psicquiatrica_frequency_combo = ttk.Combobox(treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.psicquiatrica_frequency_combo.grid(row=5, column=1)
        self.psicquiatrica_frequency_combo.config(state="disabled")
        self.psicquiatrica_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.psicquiatrica_duration_combo = ttk.Combobox(treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.psicquiatrica_duration_combo.grid(row=5, column=2)
        self.psicquiatrica_duration_combo.config(state="disabled")
        self.psicquiatrica_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.psicquiatrica_modalidad_combo = ttk.Combobox(treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.psicquiatrica_modalidad_combo.grid(row=5, column=3)
        self.psicquiatrica_modalidad_combo.config(state="disabled")
        self.psicquiatrica_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_psicquiatrica = ttk.Entry(treatment_frame)
        self.entry_psicquiatrica.grid(row=5, column=4)
        self.entry_psicquiatrica.config(state="disabled")
        self.psicquiatrica_status_combo = ttk.Combobox(treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.psicquiatrica_status_combo.grid(row=5, column=5)
        self.psicquiatrica_status_combo.config(state="disabled")
        self.psicquiatrica_status_combo.bind("<MouseWheel>", self.empty_scroll_command)

        self.otra_disciplina_var = tk.BooleanVar()
        tk.Checkbutton(treatment_frame, text="Otra:", variable=self.otra_disciplina_var, command=self.on_check_otra_disciplina).grid(row=6, column=0, sticky="w")
        self.entry_otra_disciplina = ttk.Entry(treatment_frame)
        self.entry_otra_disciplina.grid(row=7, column=0)
        self.entry_otra_disciplina.config(state="disabled")
        self.otra_disciplina_frequency_combo = ttk.Combobox(treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.otra_disciplina_frequency_combo.grid(row=7, column=1)
        self.otra_disciplina_frequency_combo.config(state="disabled")
        self.otra_disciplina_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.otra_disciplina_duration_combo = ttk.Combobox(treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.otra_disciplina_duration_combo.grid(row=7, column=2)
        self.otra_disciplina_duration_combo.config(state="disabled")
        self.otra_disciplina_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.otra_disciplina_modalidad_combo = ttk.Combobox(treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.otra_disciplina_modalidad_combo.grid(row=7, column=3)
        self.otra_disciplina_modalidad_combo.config(state="disabled")
        self.otra_disciplina_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.otra_disciplina_fisica = ttk.Entry(treatment_frame)
        self.otra_disciplina_fisica.grid(row=7, column=4)
        self.otra_disciplina_fisica.config(state="disabled")
        self.otra_disciplina_status_combo = ttk.Combobox(treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.otra_disciplina_status_combo.grid(row=7, column=5)
        self.otra_disciplina_status_combo.config(state="disabled")
        self.otra_disciplina_status_combo.bind("<MouseWheel>", self.empty_scroll_command)

    def create_historial_escolar_section(self):
        self.historial_escolar_frame = tk.LabelFrame(self.inner_frame, text="Historial escolar:", padx=10, pady=10)
        self.historial_escolar_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Historial escolar", self.historial_escolar_frame)

        self.head_start_var = tk.BooleanVar()
        self.kinderkarten_var = tk.BooleanVar()
        self.otro_programa_var = tk.BooleanVar()
        self.flunked_var = tk.BooleanVar()
        self.lectura_var = tk.BooleanVar()
        self.comprension_var = tk.BooleanVar()
        self.invierte_lectura_var = tk.BooleanVar()
        self.omite_lectura_var = tk.BooleanVar()
        self.escritura_var = tk.BooleanVar()
        self.copiar_var = tk.BooleanVar()
        self.invierte_escritura_var = tk.BooleanVar()
        self.omite_escritura_var = tk.BooleanVar()
        self.matematica_var = tk.BooleanVar()
        self.suma_var = tk.BooleanVar()
        self.multiplicacion_var = tk.BooleanVar()
        self.division_var = tk.BooleanVar()
        self.otras_dificultades_var = tk.BooleanVar()
        self.ayuda_educacion_var = tk.BooleanVar()
        self.salon_recurso_var = tk.BooleanVar()
        self.salon_completeo_var = tk.BooleanVar()
        self.otra_ayuda_var = tk.BooleanVar()
        tk.Checkbutton(self.historial_escolar_frame, text="Asistió a Head Start", variable=self.head_start_var).grid(row=0, column=0, sticky="w")
        tk.Checkbutton(self.historial_escolar_frame, text="Kindergarten", variable=self.kinderkarten_var).grid(row=0, column=1, sticky="w")
        tk.Checkbutton(self.historial_escolar_frame, text="Otro programa:", variable=self.otro_programa_var).grid(row=0, column=2, sticky="w")
        self.entry_otro_programa = tk.Entry(self.historial_escolar_frame)
        self.entry_otro_programa.grid(row=0, column=3, sticky="w")
        tk.Checkbutton(self.historial_escolar_frame, text="No fue promovido de grado, repitió:", variable=self.flunked_var, command=self.on_check_flunked).grid(row=1, column=0, columnspan=2, sticky="w")
        
        # Button to add additional entries dynamically
        self.add_entry_button = tk.Button(self.historial_escolar_frame, text="Agregar más grados", command=self.add_flunked_entry)
        self.add_entry_button.grid(row=3, column=0, sticky="w")
        self.add_entry_button.config(state="disabled")
        
        # Keep track of the dynamic entries
        self.flunked_entries = []

        tk.Label(self.historial_escolar_frame, text="1. Presenta aprovechamiento academico:").grid(row=4, column=0, columnspan=2, sticky="w")
        self.aprovechamiento_academico_combo = ttk.Combobox(self.historial_escolar_frame, values=["Satisfactorio", "Regular", "Deficiente"], state="readonly")
        self.aprovechamiento_academico_combo.grid(row=4, column=2, sticky="w")
        self.aprovechamiento_academico_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(self.historial_escolar_frame, text="2. Presenta dificultades en las áreas académicas de:").grid(row=5, column=0, columnspan=2, sticky="w")
        tk.Checkbutton(self.historial_escolar_frame, text="Lectura", variable=self.lectura_var, command=self.on_check_lectura).grid(row=6, column=0, sticky="w")
        self.comprension_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="comprensión", variable=self.comprension_var)
        self.comprension_checkbox.grid(row=6, column=1, sticky="w")
        self.comprension_checkbox.config(state=tk.DISABLED)
        self.invierte_lectura_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="invierte/sustituye", variable=self.invierte_lectura_var)
        self.invierte_lectura_checkbox.grid(row=6, column=2, sticky="w")
        self.invierte_lectura_checkbox.config(state=tk.DISABLED)
        self.omite_lectura_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="omite", variable=self.omite_lectura_var)
        self.omite_lectura_checkbox.grid(row=6, column=3, sticky="w")
        self.omite_lectura_checkbox.config(state=tk.DISABLED)
        tk.Checkbutton(self.historial_escolar_frame, text="Escritura", variable=self.escritura_var, command=self.on_check_escritura).grid(row=7, column=0, sticky="w")
        self.copiar_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="copiar/dictado", variable=self.copiar_var)
        self.copiar_checkbox.grid(row=7, column=1, sticky="w")
        self.copiar_checkbox.config(state=tk.DISABLED)
        self.invierte_escritura_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="invierte/sustituye", variable=self.invierte_escritura_var)
        self.invierte_escritura_checkbox.grid(row=7, column=2, sticky="w")
        self.invierte_escritura_checkbox.config(state=tk.DISABLED)
        self.omite_escritura_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="omite", variable=self.omite_escritura_var)
        self.omite_escritura_checkbox.grid(row=7, column=3, sticky="w")
        self.omite_escritura_checkbox.config(state=tk.DISABLED)
        tk.Checkbutton(self.historial_escolar_frame, text="Matemáticas", variable=self.matematica_var, command=self.on_check_matematicas).grid(row=8, column=0, sticky="w")
        self.suma_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="suma/resta", variable=self.suma_var)
        self.suma_checkbox.grid(row=8, column=1, sticky="w")
        self.suma_checkbox.config(state=tk.DISABLED)
        self.multiplicacion_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="multiplicación", variable=self.multiplicacion_var)
        self.multiplicacion_checkbox.grid(row=8, column=2, sticky="w")
        self.multiplicacion_checkbox.config(state=tk.DISABLED)
        self.division_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="división", variable=self.division_var)
        self.division_checkbox.grid(row=8, column=3, sticky="w")
        self.division_checkbox.config(state=tk.DISABLED)
        tk.Checkbutton(self.historial_escolar_frame, text="Otras dificultades:", variable=self.otras_dificultades_var, command=self.on_check_otras_dificultades).grid(row=9, column=0, sticky="w")
        self.entry_otras_dificultades = tk.Entry(self.historial_escolar_frame)
        self.entry_otras_dificultades.grid(row=9, column=1, columnspan=2, sticky="w")
        self.entry_otras_dificultades.config(state=tk.DISABLED)

        self.ayuda_educacion_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="3. Recibe ayuda del Programa de Educación Especial", variable=self.ayuda_educacion_var, command=self.on_check_ayuda_educacion)
        self.ayuda_educacion_checkbox.grid(row=10, column=0, columnspan=2, sticky="w")
        self.salon_recurso_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="Salón Recurso", variable=self.salon_recurso_var)
        self.salon_recurso_checkbox.grid(row=11, column=0, sticky="w")
        self.salon_recurso_checkbox.config(state=tk.DISABLED)
        self.salon_completo_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="Salón a tiempo completo", variable=self.salon_completeo_var)
        self.salon_completo_checkbox.grid(row=11, column=1, sticky="w")
        self.salon_completo_checkbox.config(state=tk.DISABLED)
        self.otra_ayuda_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="Otra (especifique):", variable=self.otra_ayuda_var, command=self.on_check_otra_ayuda)
        self.otra_ayuda_checkbox.grid(row=11, column=2, sticky="w")
        self.otra_ayuda_checkbox.config(state=tk.DISABLED)
        self.entry_otra_ayuda = tk.Entry(self.historial_escolar_frame)
        self.entry_otra_ayuda.grid(row=11, column=3, sticky="w")
        self.entry_otra_ayuda.config(state=tk.DISABLED)

        tk.Label(self.historial_escolar_frame, text="4. Funcionamiento académico actual:").grid(row=12, column=0, columnspan=2, sticky="w")
        self.entry_funcionamiento_academico = tk.Entry(self.historial_escolar_frame)
        self.entry_funcionamiento_academico.grid(row=13, column=0, columnspan=4, sticky="we")
    
    def create_relaciones_interpersonales_section(self):
        relaciones_interpersonales_frame = tk.LabelFrame(self.inner_frame, text="Relaciones interpersonales:", padx=10, pady=10)
        relaciones_interpersonales_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Relaciones interpersonales", relaciones_interpersonales_frame)

        ri_combo_options = ["Adecuada", "No adecuada"]
        tk.Label(relaciones_interpersonales_frame, text="Relaciones con sus padres o encargados").grid(row=0, column=0, columnspan=2, sticky="w")
        self.relaciones_padres_combo = ttk.Combobox(relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_padres_combo.grid(row=0, column=2, sticky="w")
        self.relaciones_padres_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(relaciones_interpersonales_frame, text="Relaciones con sus hermanos").grid(row=1, column=0, columnspan=2, sticky="w")
        self.relaciones_hermanos_combo = ttk.Combobox(relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_hermanos_combo.grid(row=1, column=2, sticky="w")
        self.relaciones_hermanos_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(relaciones_interpersonales_frame, text="Relaciones con su grupo de pares").grid(row=2, column=0, columnspan=2, sticky="w")
        self.relaciones_grupo_combo = ttk.Combobox(relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_grupo_combo.grid(row=2, column=2, sticky="w")
        self.relaciones_grupo_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(relaciones_interpersonales_frame, text="Relaciones con los adultos").grid(row=3, column=0, columnspan=2, sticky="w")
        self.relaciones_adultos_combo = ttk.Combobox(relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_adultos_combo.grid(row=3, column=2, sticky="w")
        self.relaciones_adultos_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(relaciones_interpersonales_frame, text="Relaciones con figuras de autoridad").grid(row=4, column=0, columnspan=2, sticky="w")
        self.relaciones_autoridad_combo = ttk.Combobox(relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_autoridad_combo.grid(row=4, column=2, sticky="w")
        self.relaciones_autoridad_combo.bind("<MouseWheel>", self.empty_scroll_command)

    def create_salud_actual_section(self):
        salud_acutal_frame = tk.LabelFrame(self.inner_frame, text="Salud actual:", padx=10, pady=10)
        salud_acutal_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Salud actual", salud_acutal_frame)
        self.buena_salud_var = tk.BooleanVar()
        self.problemas_visuales_var = tk.BooleanVar()
        self.espejuelos_var = tk.BooleanVar()
        self.problemas_auditivos_var = tk.BooleanVar()
        self.audifonos_var = tk.BooleanVar()
        self.neuro_problems_var = tk.BooleanVar()
        self.problemas_motores_var = tk.BooleanVar()
        self.silla_ruedas_var = tk.BooleanVar()
        self.protesis_var = tk.BooleanVar()
        self.tratamiento_medico_var = tk.BooleanVar()
        self.otros_problemas_salud_var = tk.BooleanVar()
        self.salud_actual_vars = {
            "Buena": self.buena_salud_var,
            "Problemas visuales": self.problemas_visuales_var,
            "Usa espejuelos": self.espejuelos_var,
            "Problemas auditivos": self.problemas_auditivos_var,
            "Usa audífonos": self.audifonos_var,
            "Problemas neurológicos": self.neuro_problems_var,
            "Problemas motores": self.problemas_motores_var,
            "Usa silla de ruedas": self.silla_ruedas_var,
            "Usa prótesis": self.protesis_var,
            "Recibe tratamiento médico:": self.tratamiento_medico_var,
            "Otros problemas de salud:": self.otros_problemas_salud_var,
        }
        row = 0
        column = 0
        for label, var in self.salud_actual_vars.items():
            if label == "Recibe tratamiento médico:":
                tk.Checkbutton(salud_acutal_frame, text=label, variable=var, command=self.on_check_tratamiento_medico).grid(row=row, column=column, sticky="w", padx=5, pady=5)
                self.entry_tratamiento_medico = tk.Entry(salud_acutal_frame)
                column +=1
                self.entry_tratamiento_medico.grid(row=row, column=column, sticky="w")
                self.entry_tratamiento_medico.config(state=tk.DISABLED)
            elif label == "Otros problemas de salud:":
                tk.Checkbutton(salud_acutal_frame, text=label, variable=var, command=self.on_check_otros_problemas_salud).grid(row=row, column=column, sticky="w", padx=5, pady=5)
                self.entry_otros_problemas_salud = tk.Entry(salud_acutal_frame)
                column +=1
                self.entry_otros_problemas_salud.grid(row=row, column=column, sticky="w")
                self.entry_otros_problemas_salud.config(state=tk.DISABLED)
            else:
                tk.Checkbutton(salud_acutal_frame, text=label, variable=var).grid(row=row, column=column, sticky="w", padx=5, pady=5)
            if column >= 2:
                column = 0
                row += 1
            else:
                column += 1

    def create_conducta_section(self):
        conducta_frame = tk.LabelFrame(self.inner_frame, text="Conducta:", padx=10, pady=10)
        conducta_frame.pack(fill="x", padx=10, pady=5)

        self.create_toggle_button("Conducta", conducta_frame)
        self.miedo_escuela_var = tk.BooleanVar()
        self.enuresis_var = tk.BooleanVar()
        self.tic_nervioso_var = tk.BooleanVar()
        self.retraimiento_var = tk.BooleanVar()
        self.encopresis_var = tk.BooleanVar()
        self.tristeza_var = tk.BooleanVar()
        self.agresividad_var = tk.BooleanVar()
        self.come_unas_var = tk.BooleanVar()
        self.llantos_var = tk.BooleanVar()
        self.andisedad_var = tk.BooleanVar()
        self.auto_agresion_var = tk.BooleanVar()
        self.reta_autoridad_var = tk.BooleanVar()
        self.irritabilidad_var = tk.BooleanVar()
        self.desafiante_var = tk.BooleanVar()
        self.impulsividad_var = tk.BooleanVar()
        self.otros_rasgos_var = tk.BooleanVar()

        self.conducta_vars = {
            "Miedo a asistir a la escuela": self.miedo_escuela_var,
            "Enuresis": self.enuresis_var,
            "Tic nervioso": self.tic_nervioso_var,
            "Retraimiento": self.retraimiento_var,
            "Encopresis": self.encopresis_var,
            "Tristeza": self.tristeza_var,
            "Agresividad": self.agresividad_var,
            "Se come las uñas": self.come_unas_var,
            "Llantos frecuentes": self.llantos_var,
            "Ansiedad": self.andisedad_var, 
            "Se auto agrede": self.auto_agresion_var, 
            "Reta la autoridad": self.reta_autoridad_var,
            "Irritabilidad": self.irritabilidad_var, 
            "Desafiante": self.desafiante_var,
            "Impulsividad": self.impulsividad_var,
            "Otros rasgos de conducta:": self.otros_rasgos_var,
        }

        row = 0
        column = 0
        for label, var in self.conducta_vars.items():
            if label == "Otros rasgos de conducta:":
                tk.Checkbutton(conducta_frame, text=label, variable=var, command=self.on_check_otros_rasgos).grid(row=row, column=column, sticky="w", padx=5, pady=5)
                self.entry_otros_rasgos = tk.Entry(conducta_frame)
                column +=1
                self.entry_otros_rasgos.grid(row=row, column=column, sticky="w")
                self.entry_otros_rasgos.config(state=tk.DISABLED)
            else:
                tk.Checkbutton(conducta_frame, text=label, variable=var).grid(row=row, column=column, sticky="w", padx=5, pady=5)
            if column >= 4:
                column = 0
                row += 1
            else:
                column += 1

    def create_toggle_button(self, text, frame):
        toggle_button = tk.Button(self.inner_frame, text=f"Toggle {text}", command=lambda: self.toggle_section(frame), relief=tk.FLAT)
        toggle_button.pack(pady=2, anchor="e")

    def submit_form(self):
        # Collect and process form data
        """Edit submit button action."""
        messagebox.showinfo("submit", "submit functionality will be implemented.")

    def close_window(self):
        """Properly close the Toplevel window and re-enable the main window."""
        self.parent.grab_release()
        self.parent.attributes('-disabled', False)
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

    def on_check_habla(self):
        if self.habla_var.get():
            self.habla_duration_combo.config(state="normal")
            self.habla_frequency_combo.config(state="normal")
            self.habla_modalidad_combo.config(state="normal")
            self.habla_status_combo.config(state="normal")
            self.entry_habla.config(state="normal")
        else:
            self.habla_duration_combo.delete(0, tk.END)
            self.habla_duration_combo.config(state="disabled")
            self.habla_frequency_combo.delete(0, tk.END)
            self.habla_frequency_combo.config(state="disabled")
            self.habla_status_combo.delete(0, tk.END)
            self.habla_status_combo.config(state="disabled")
            self.habla_modalidad_combo.delete(0, tk.END)
            self.habla_modalidad_combo.config(state="disabled")
            self.entry_habla.delete(0, tk.END)
            self.entry_habla.config(state="disabled")

    def on_check_ocupacional(self):
        if self.ocupacional_var.get():
            self.ocupacional_duration_combo.config(state="normal")
            self.ocupacional_frequency_combo.config(state="normal")
            self.ocupacional_modalidad_combo.config(state="normal")
            self.ocupacional_status_combo.config(state="normal")
            self.entry_ocupacional.config(state="normal")
        else:
            self.ocupacional_duration_combo.delete(0, tk.END)
            self.ocupacional_duration_combo.config(state="disabled")
            self.ocupacional_frequency_combo.delete(0, tk.END)
            self.ocupacional_frequency_combo.config(state="disabled")
            self.ocupacional_status_combo.delete(0, tk.END)
            self.ocupacional_status_combo.config(state="disabled")
            self.ocupacional_modalidad_combo.delete(0, tk.END)
            self.ocupacional_modalidad_combo.config(state="disabled")
            self.entry_ocupacional.delete(0, tk.END)
            self.entry_ocupacional.config(state="disabled")

    def on_check_psicologica(self):
        if self.psicologica_var.get():
            self.psicologica_duration_combo.config(state="normal")
            self.psicologica_frequency_combo.config(state="normal")
            self.psicologica_modalidad_combo.config(state="normal")
            self.psicologica_status_combo.config(state="normal")
            self.entry_psicologica.config(state="normal")
        else:
            self.psicologica_duration_combo.delete(0, tk.END)
            self.psicologica_duration_combo.config(state="disabled")
            self.psicologica_frequency_combo.delete(0, tk.END)
            self.psicologica_frequency_combo.config(state="disabled")
            self.psicologica_status_combo.delete(0, tk.END)
            self.psicologica_status_combo.config(state="disabled")
            self.psicologica_modalidad_combo.delete(0, tk.END)
            self.psicologica_modalidad_combo.config(state="disabled")
            self.entry_psicologica.delete(0, tk.END)
            self.entry_psicologica.config(state="disabled")

    def on_check_fisica(self):
        if self.fisica_var.get():
            self.fisica_duration_combo.config(state="normal")
            self.fisica_frequency_combo.config(state="normal")
            self.fisica_modalidad_combo.config(state="normal")
            self.fisica_status_combo.config(state="normal")
            self.entry_fisica.config(state="normal")
        else:
            self.fisica_duration_combo.delete(0, tk.END)
            self.fisica_duration_combo.config(state="disabled")
            self.fisica_frequency_combo.delete(0, tk.END)
            self.fisica_frequency_combo.config(state="disabled")
            self.fisica_status_combo.delete(0, tk.END)
            self.fisica_status_combo.config(state="disabled")
            self.fisica_modalidad_combo.delete(0, tk.END)
            self.fisica_modalidad_combo.config(state="disabled")
            self.entry_fisica.delete(0, tk.END)
            self.entry_fisica.config(state="disabled")

    def on_check_psicquiatrica(self):
        if self.psicquiatrica_var.get():
            self.psicquiatrica_duration_combo.config(state="normal")
            self.psicquiatrica_frequency_combo.config(state="normal")
            self.psicquiatrica_modalidad_combo.config(state="normal")
            self.psicquiatrica_status_combo.config(state="normal")
            self.entry_psicquiatrica.config(state="normal")
        else:
            self.psicquiatrica_duration_combo.delete(0, tk.END)
            self.psicquiatrica_duration_combo.config(state="disabled")
            self.psicquiatrica_frequency_combo.delete(0, tk.END)
            self.psicquiatrica_frequency_combo.config(state="disabled")
            self.psicquiatrica_status_combo.delete(0, tk.END)
            self.psicquiatrica_status_combo.config(state="disabled")
            self.psicquiatrica_modalidad_combo.delete(0, tk.END)
            self.psicquiatrica_modalidad_combo.config(state="disabled")
            self.entry_psicquiatrica.delete(0, tk.END)
            self.entry_psicquiatrica.config(state="disabled")

    def on_check_otra_disciplina(self):
        if self.otra_disciplina_var.get():
            self.otra_disciplina_duration_combo.config(state="normal")
            self.otra_disciplina_frequency_combo.config(state="normal")
            self.otra_disciplina_modalidad_combo.config(state="normal")
            self.otra_disciplina_status_combo.config(state="normal")
            self.entry_otra_disciplina.config(state="normal")
            self.otra_disciplina_fisica.config(state="normal")
        else:
            self.otra_disciplina_duration_combo.delete(0, tk.END)
            self.otra_disciplina_duration_combo.config(state="disabled")
            self.otra_disciplina_frequency_combo.delete(0, tk.END)
            self.otra_disciplina_frequency_combo.config(state="disabled")
            self.otra_disciplina_status_combo.delete(0, tk.END)
            self.otra_disciplina_status_combo.config(state="disabled")
            self.otra_disciplina_modalidad_combo.delete(0, tk.END)
            self.otra_disciplina_modalidad_combo.config(state="disabled")
            self.entry_otra_disciplina.delete(0, tk.END)
            self.entry_otra_disciplina.config(state="disabled")
            self.otra_disciplina_fisica.delete(0, tk.END)
            self.otra_disciplina_fisica.config(state="disabled")
     
    def on_check_flunked(self):
        """Handles the first time entries for grade and times repeated."""
        if self.flunked_var.get():
            # Frame to hold dynamic grade and times entries
            self.flunked_entries_frame = tk.Frame(self.historial_escolar_frame)
            self.flunked_entries_frame.grid(row=2, column=0, columnspan=4, sticky="w")
            self.add_flunked_entry()
            self.add_entry_button.config(state="normal")
        else:
            self.clear_flunked_entries()
            self.add_entry_button.config(state="disabled")
            self.flunked_entries_frame.destroy()

    def add_flunked_entry(self):
        """Adds a new set of grade and times repeated entries."""
        row = len(self.flunked_entries)

        # Grade entry
        grade_label = tk.Label(self.flunked_entries_frame, text=f"Grado {row + 1}:")
        grade_label.grid(row=row, column=0, sticky="w")
        grade_entry = tk.Entry(self.flunked_entries_frame)
        grade_entry.grid(row=row, column=1, sticky="w")

        # Times repeated entry
        times_label = tk.Label(self.flunked_entries_frame, text="Veces:")
        times_label.grid(row=row, column=2, sticky="w")
        times_entry = tk.Entry(self.flunked_entries_frame, width=5)
        times_entry.grid(row=row, column=3, sticky="w")

        # Store the entries to access them later if needed
        self.flunked_entries.append((grade_entry, times_entry))
    
    def clear_flunked_entries(self):
        """Clears all widgets within the flunked entries frame."""
        for widget in self.flunked_entries_frame.winfo_children():
            widget.destroy()
        self.flunked_entries.clear()

    def on_check_lectura(self):
        if self.lectura_var.get():
            self.comprension_checkbox.config(state=tk.NORMAL)
            self.invierte_lectura_checkbox.config(state=tk.NORMAL)
            self.omite_lectura_checkbox.config(state=tk.NORMAL)
        else:
            self.comprension_var.set(tk.FALSE)
            self.invierte_lectura_var.set(tk.FALSE)
            self.omite_lectura_var.set(tk.FALSE)
            self.comprension_checkbox.config(state=tk.DISABLED)
            self.invierte_lectura_checkbox.config(state=tk.DISABLED)
            self.omite_lectura_checkbox.config(state=tk.DISABLED)
    
    def on_check_escritura(self):
        if self.escritura_var.get():
            self.copiar_checkbox.config(state=tk.NORMAL)
            self.invierte_escritura_checkbox.config(state=tk.NORMAL)
            self.omite_escritura_checkbox.config(state=tk.NORMAL)
        else:
            self.copiar_var.set(tk.FALSE)
            self.invierte_escritura_var.set(tk.FALSE)
            self.omite_escritura_var.set(tk.FALSE)
            self.copiar_checkbox.config(state=tk.DISABLED)
            self.invierte_escritura_checkbox.config(state=tk.DISABLED)
            self.omite_escritura_checkbox.config(state=tk.DISABLED)

    def on_check_matematicas(self):
        if self.matematica_var.get():
            self.suma_checkbox.config(state=tk.NORMAL)
            self.multiplicacion_checkbox.config(state=tk.NORMAL)
            self.division_checkbox.config(state=tk.NORMAL)
        else:
            self.suma_var.set(tk.FALSE)
            self.multiplicacion_var.set(tk.FALSE)
            self.division_var.set(tk.FALSE)
            self.suma_checkbox.config(state=tk.DISABLED)
            self.multiplicacion_checkbox.config(state=tk.DISABLED)
            self.division_checkbox.config(state=tk.DISABLED)

    def on_check_otras_dificultades(self):
        if self.otras_dificultades_var.get():
            self.entry_otras_dificultades.config(state=tk.NORMAL)
        else:
            self.entry_otras_dificultades.delete(0, tk.END)
            self.entry_otras_dificultades.config(state=tk.DISABLED)

    def on_check_ayuda_educacion(self):
        if self.ayuda_educacion_var.get():
            self.salon_recurso_checkbox.config(state=tk.NORMAL)
            self.salon_completo_checkbox.config(state=tk.NORMAL)
            self.otra_ayuda_checkbox.config(state=tk.NORMAL)
        else:
            if self.otra_ayuda_var.get():
                self.entry_otra_ayuda.delete(0, tk.END)
                self.entry_otra_ayuda.config(state=tk.DISABLED)
            self.salon_recurso_var.set(tk.FALSE)
            self.salon_completeo_var.set(tk.FALSE)
            self.otra_ayuda_var.set(tk.FALSE)
            self.salon_recurso_checkbox.config(state=tk.DISABLED)
            self.salon_completo_checkbox.config(state=tk.DISABLED)
            self.otra_ayuda_checkbox.config(state=tk.DISABLED)
    
    def on_check_otra_ayuda(self):
        if self.otra_ayuda_var.get():
            self.entry_otra_ayuda.config(state=tk.NORMAL)
        else:
            self.entry_otra_ayuda.delete(0, tk.END)
            self.entry_otra_ayuda.config(state=tk.DISABLED)

    def on_check_tratamiento_medico(self):
        if self.tratamiento_medico_var.get():
            self.entry_tratamiento_medico.config(state=tk.NORMAL)
        else:
            self.entry_tratamiento_medico.delete(0, tk.END)
            self.entry_tratamiento_medico.config(state=tk.DISABLED)

    def on_check_otros_problemas_salud(self):
        if self.otros_problemas_salud_var.get():
            self.entry_otros_problemas_salud.config(state=tk.NORMAL)
        else:
            self.entry_otros_problemas_salud.delete(0, tk.END)
            self.entry_otros_problemas_salud.config(state=tk.DISABLED)

    def on_check_otros_rasgos(self):
        if self.otros_rasgos_var.get():
            self.entry_otros_rasgos.config(state=tk.NORMAL)
        else:
            self.entry_otros_rasgos.delete(0, tk.END)
            self.entry_otros_rasgos.config(state=tk.DISABLED)
# For testing the form
if __name__ == "__main__":
    root = tk.Tk()
    app = AddPatientForm(root, parent=None)
    root.mainloop()