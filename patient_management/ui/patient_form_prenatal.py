import tkinter as tk   
import logging
from ..utils.logging_config import setup_logging

class PrenatalSection:
    def __init__(self, parent_frame):
         #Setup logging
         setup_logging()
         self.logger = logging.getLogger(__name__)
         """Initialize and create the main section with all fields."""
         self.widgets = {}
         self.create_prenatal_history_section(parent_frame)
         self.create_perinatal_history_section(parent_frame)

    def create_prenatal_history_section(self, parent_frame):
        prenatal_frame = tk.LabelFrame(parent_frame, text="Historial Prenatal", padx=10, pady=10)
        prenatal_frame.pack(fill="x", padx=10, pady=5)
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
            "Otras enfermedades:": tk.BooleanVar(),
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
        self.estado_emocional_var = tk.BooleanVar()
        self.estado_emocional_cb = tk.Checkbutton(prenatal_frame, text="Estado emocional de la madre:", variable=self.estado_emocional_var, command=self.on_check_estado_emocional)
        self.estado_emocional_cb.grid(row=row + 1, column=0, sticky="w")
        self.entry_mother_emotional_state = tk.Entry(prenatal_frame)
        self.entry_mother_emotional_state.grid(row=row + 1, column=1, sticky="w", padx=5, pady=5)
        self.entry_mother_emotional_state.config(state="disabled")

    def create_perinatal_history_section(self, parent_frame):
        perinatal_frame = tk.LabelFrame(parent_frame, text="Historial perinatal", padx=10, pady=10)
        perinatal_frame.pack(fill="x", padx=10, pady=5)

        self.parto_natural_var = tk.BooleanVar()
        self.parto_cesarea_var = tk.BooleanVar()
        self.parto_prematuro_var = tk.BooleanVar()

        self.parto_natural_cb = tk.Checkbutton(perinatal_frame, text="Parto Natural", variable=self.parto_natural_var).grid(row=0, column=0, sticky="w")
        self.parto_cesarea_cb = tk.Checkbutton(perinatal_frame, text="Parto Cesárea", variable=self.parto_cesarea_var).grid(row=0, column=1, sticky="w")
        self.parto_prematuro_cb = tk.Checkbutton(perinatal_frame, text="Parto prematuro", variable=self.parto_prematuro_var).grid(row=0, column=2, sticky="w")
        self.complicaciones_var = tk.BooleanVar()
        self.parto_complications_cb = tk.Checkbutton(perinatal_frame, text="Complicaciones durante el parto:", variable=self.complicaciones_var, command=self.on_check_complications).grid(row=1, column=0, sticky="w")

        self.entry_complications = tk.Entry(perinatal_frame, state="disabled")
        self.entry_complications.grid(row=1, column=1, sticky="w")

    def on_check_otras_enfermedades(self):
        if self.prenatal_vars["Otras enfermedades:"].get():
            self.entry_other_illnesses.config(state="normal")
        else:
            self.entry_other_illnesses.delete(0, tk.END)
            self.entry_other_illnesses.config(state="disabled")

    def on_check_complications(self):
        if self.complicaciones_var.get():
            self.entry_complications.config(state="normal")
        else:
            self.entry_complications.delete(0, tk.END)
            self.entry_complications.config(state="disabled")

    def on_check_estado_emocional(self):
        self.logger.info("on_check_estado_emocional entered")
        if self.estado_emocional_var.get():
            self.entry_mother_emotional_state.config(state="normal")
        else:
            self.entry_mother_emotional_state.delete(0, tk.END)
            self.entry_mother_emotional_state.config(state="disabled")
    
    def get_values(self):
        return {
            "prenatal_normal": self.prenatal_vars["Normal"].get(),
            "prenatal_falls": self.prenatal_vars["Caídas"].get(),
            "prenatal_druguse": self.prenatal_vars["Uso de drogas, alcohol"].get(),
            "prenatal_high_bp": self.prenatal_vars["Alta presión"].get(),
            "prenatal_bleeds": self.prenatal_vars["Sangrado"].get(),
            "prenatal_vomits": self.prenatal_vars["Vómitos frecuentes"].get(),
            "prenatal_diabetes": self.prenatal_vars["Diabetes"].get(),
            "prenatal_accidents": self.prenatal_vars["Accidentes"].get(),
            "prenatal_meduse": self.prenatal_vars["Uso de Medicamentos"].get(),
            "prenatal_other": self.prenatal_vars["Otras enfermedades:"].get(),
            "prenatal_other_text": self.entry_other_illnesses.get(),
            "prenatal_mothers_emotional_state": self.estado_emocional_var.get(),
            "prenatal_mothers_emotional_state_text": self.entry_mother_emotional_state.get(),
            "perinatal_natural": self.parto_natural_var.get(),
            "perinatal_csection": self.parto_cesarea_var.get(),
            "perinatal_premature": self.parto_prematuro_var.get(),
            "perinatal_complications": self.complicaciones_var.get(),
            "perinatal_complications_text": self.entry_complications.get()
        }