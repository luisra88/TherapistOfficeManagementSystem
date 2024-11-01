import tkinter as tk
from tkinter import ttk


class PostnatalSection:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.widgets = {}
        self.create_postnatal_history_section(parent_frame)

    def create_postnatal_history_section(self, parent_frame):
        self.postnatal_frame = tk.LabelFrame(parent_frame, text="Historial Postnatal", padx=10, pady=10)
        self.postnatal_frame.pack(fill="x", padx=10, pady=5)


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
                tk.Label(self.postnatal_frame, text="Tiempo:").grid(row=row, column=column+1, sticky="e")
                self.entry_incubator_time = tk.Entry(self.postnatal_frame)
                self.entry_incubator_time.grid(row=row, column=column+2)
                self.entry_incubator_time.config(state="disabled")
                tk.Checkbutton(self.postnatal_frame, text=label, variable=var, command=self.on_check_incubadora).grid(row=row, column=column, sticky="w")
            elif label=="Otras Condiciones:":
                tk.Checkbutton(self.postnatal_frame, text=label, variable=var, command=self.on_check_otras_condiciones).grid(row=row, column=column, sticky="w")
            else:
                tk.Checkbutton(self.postnatal_frame, text=label, variable=var).grid(row=row, column=column, sticky="w")
            if column == 2:
                column = 0
                row += 1
            else:
                column += 1

        self.entry_other_conditions = tk.Entry(self.postnatal_frame)
        self.entry_other_conditions.grid(row=row, column=1)
        self.entry_other_conditions.config(state="disabled")

        # Weight at birth
        tk.Label(self.postnatal_frame, text="Peso al nacer:").grid(row=row + 2, column=0, sticky="w")
        tk.Label(self.postnatal_frame, text="libras").grid(row=row + 2, column=2, sticky="w")
        self.entry_weight_at_birth_pounds = tk.Entry(self.postnatal_frame)
        self.entry_weight_at_birth_pounds.grid(row=row + 2, column=1)
        tk.Label(self.postnatal_frame, text="onzas").grid(row=row + 2, column=4, sticky="w")
        self.entry_weight_at_birth_oz = tk.Entry(self.postnatal_frame)
        self.entry_weight_at_birth_oz.grid(row=row + 2, column=3)

        # Size at birth
        tk.Label(self.postnatal_frame, text="Tamaño al nacer:").grid(row=row + 3, column=0, sticky="w")
        tk.Label(self.postnatal_frame, text="pulgadas").grid(row=row + 3, column=2, sticky="w")
        self.entry_size_at_birth = tk.Entry(self.postnatal_frame)
        self.entry_size_at_birth.grid(row=row + 3, column=1)

        tk.Label(self.postnatal_frame, text="Desarrollo").grid(row=row + 4, column=0, sticky="w")

        # Psycholinguistic Development
        tk.Label(self.postnatal_frame, text="Desarrollo psicolinguistico:").grid(row=row + 5, column=0, sticky="w")
        self.psycholinguistic_dev = ttk.Combobox(self.postnatal_frame, values=["Normal", "Rápido", "Lento"], state="readonly")
        self.psycholinguistic_dev.grid(row=row + 5, column=1)
        self.psycholinguistic_dev.bind("<MouseWheel>", self.empty_scroll_command)
        self.psycholinguistic_dev_var = tk.BooleanVar()
        tk.Checkbutton(self.postnatal_frame, text="Dificultad en:", variable=self.psycholinguistic_dev_var, command=self.on_psycholinguistic_difficulty_check).grid(row=row+5, column=2, sticky="w")
        self.entry_psycholinguistic_difficulties = tk.Entry(self.postnatal_frame, state = "disabled")
        self.entry_psycholinguistic_difficulties.grid(row=row + 5, column=3)

        # Psychomotor Development
        tk.Label(self.postnatal_frame, text="Desarrollo psicomotor:").grid(row=row + 7, column=0, sticky="w")
        self.psychomotor_dev = ttk.Combobox(self.postnatal_frame, values=["Normal", "Rápido", "Lento"], state="readonly")
        self.psychomotor_dev.grid(row=row + 7, column=1)
        self.psychomotor_dev.bind("<MouseWheel>", self.empty_scroll_command)
        self.psychomotor_dev_var = tk.BooleanVar()
        tk.Checkbutton(self.postnatal_frame, text="Dificultad en:", variable=self.psychomotor_dev_var, command=self.on_psychomotor_difficulty_check).grid(row=row+7, column=2, sticky="w")
        self.entry_psychomotor_difficulties = tk.Entry(self.postnatal_frame, state="disabled")
        self.entry_psychomotor_difficulties.grid(row=row + 7, column=3)

        # Activity level
        tk.Label(self.postnatal_frame, text="Nivel de actividad").grid(row=row + 9, column=0, sticky="w")
        self.activity_level = ttk.Combobox(self.postnatal_frame, values=["Tranquilo", "Inquieto", "Hiperactivo", "Hipoactivo"], state="readonly")
        self.activity_level.grid(row=row + 9, column=1)
        self.activity_level.bind("<MouseWheel>", self.empty_scroll_command)

        # Development milestones
        tk.Label(self.postnatal_frame, text="Especifique a qué edad llevó a cabo las siguientes actividades:").grid(row=row+10, column=0, columnspan=2, sticky="nsew")
        tk.Label(self.postnatal_frame, text="Clave: (L) lento    (AN) aparentemente normal    (NL) no logrado").grid(row=row+11, column=0, columnspan=2, sticky="nsew")
         # List of milestones
        milestones = [
            "Virarse", "Sentarse", "Gatear", "Caminar", "Pararse con soporte",
            "Pararse sin soporte", "Brincar en un pie", "Brincar en ambos pies", "Saltar", "Jugar"
        ]

        # Combobox options
        options = ["L", "AN", "NL"]

        # Loop through the milestones and create corresponding labels and comboboxes
        self.milestone_vars = {}  # Dictionary to store the Combobox variables for later use
        milestones_column = 0
        for milestone in milestones:
            tk.Label(self.postnatal_frame, text=milestone + ":").grid(row=row+12, column=milestones_column, sticky="w")
            
            # Create a Combobox for each milestone
            combobox = ttk.Combobox(self.postnatal_frame, values=options, state="readonly")
            combobox.grid(row=row+12, column=milestones_column+1, padx=5, pady=2)
            combobox.bind("<MouseWheel>", self.empty_scroll_command)
            
            # Store the combobox in the dictionary with the milestone as the key
            self.milestone_vars[milestone] = combobox
            if(milestones_column == 0):
                milestones_column =2
            else:
                milestones_column = 0
                row += 1

    def empty_scroll_command(self, event):
        """Pass scroll event to the parent frame."""
        self.postnatal_frame.master.event_generate("<MouseWheel>", delta=event.delta)
        return "break"
    
    def on_psycholinguistic_difficulty_check(self):
        selected_value = self.psycholinguistic_dev_var.get()
        if selected_value:
            # Enable the entry field
            self.entry_psycholinguistic_difficulties.config(state="normal")
        else:
            # Disable the entry field for other selections
            self.entry_psycholinguistic_difficulties.delete(0, tk.END) 
            self.entry_psycholinguistic_difficulties.config(state="disabled")   

    def on_psychomotor_difficulty_check(self):
        selected_value = self.psychomotor_dev_var.get()
        if selected_value:
            # Enable the entry field
            self.entry_psychomotor_difficulties.config(state="normal")
        else:
            # Disable the entry field for other selections
            self.entry_psychomotor_difficulties.delete(0, tk.END)   
            self.entry_psychomotor_difficulties.config(state="disabled")
    
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
    
    def get_postnatal_values(self):
        return {
            "postnatal_normal": self.normal_var.get(),
            "postnatal_cianosis": self.cianosis_var.get(),
            "postnatal_meningitis": self.meningitis_var.get(),
            "postnatal_ictericia": self.ictericia_var.get(),
            "postnatal_seizures": self.convulciones_var.get(),
            "postnatal_incubator": self.incubadora_var.get(),
            "postnatal_incubator_time": self.entry_incubator_time.get(),
            "postnatal_other": self.otras_condiciones_var.get(),
            "postnatal_other_text": self.entry_other_conditions.get(),
            "weight_pounds": self.entry_weight_at_birth_pounds.get(),
            "weight_oz": self.entry_weight_at_birth_oz.get(),
            "size_at_birth": self.entry_size_at_birth.get()
        }
    
    def get_development_values(self):
        return {
            "psycholinguistic_development": self.psycholinguistic_dev.get(),
            "psycholinguistic_difficulty": self.psycholinguistic_dev_var.get(),
            "pshycholinguistic_difficulty_text": self.entry_psycholinguistic_difficulties.get(),
            "psychomotor_development": self.psychomotor_dev.get(),
            "psychomotor_difficulty": self.psychomotor_dev_var.get(),
            "psychomotor_difficulty_text": self.entry_psychomotor_difficulties.get(),
            "psychomotor_dactivity_levelifficulty_text": self.activity_level.get(),
            "turn_level": self.milestone_vars["Virarse"].get(),
            "sit_level": self.milestone_vars["Sentarse"].get(),
            "crawl_level": self.milestone_vars["Gatear"].get(),
            "walk_level": self.milestone_vars["Caminar"].get(),
            "stand_with_support_level": self.milestone_vars["Pararse con soporte"].get(),
            "stand_without_support_level": self.milestone_vars["Pararse sin soporte"].get(),
            "jump_with_one_foot_level": self.milestone_vars["Brincar en un pie"].get(),
            "jump_with_both_feet_level": self.milestone_vars["Brincar en ambos pies"].get(),
            "leap_level": self.milestone_vars["Saltar"].get(),
            "play_level": self.milestone_vars["Jugar"].get()
        }
    