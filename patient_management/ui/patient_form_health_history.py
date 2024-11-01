    
import tkinter as tk
from tkinter import ttk

class HealthHistory:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.create_salud_actual_section(parent_frame)
    def create_salud_actual_section(self, parent_frame):
        salud_acutal_frame = tk.LabelFrame(parent_frame, text="Salud actual:", padx=10, pady=10)
        salud_acutal_frame.pack(fill="x", padx=10, pady=5)

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

    def get_current_health_values(self):
        return {
            "good_health": self.buena_salud_var.get(),
            "visual_problems": self.problemas_visuales_var.get(),
            "uses_glasses": self.espejuelos_var.get(),
            "hearing_problems": self.problemas_auditivos_var.get(),
            "uses_hearing_aids": self.audifonos_var.get(),
            "neurological_problems": self.neuro_problems_var.get(),
            "motor_problems": self.problemas_motores_var.get(),
            "uses_wheelchair": self.silla_ruedas_var.get(),
            "uses_prosthesis": self.protesis_var.get(),
            "medical_treatment": self.tratamiento_medico_var.get(),
            "medical_treatment_text": self.entry_tratamiento_medico.get(),
            "other_health_issues": self.otros_problemas_salud_var.get(),
            "other_health_issues_text": self.entry_otros_problemas_salud.get()
        }