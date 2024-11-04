import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class BehaviorSection:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.create_behavior_section(parent_frame)    
    def create_behavior_section(self, parent_frame):
        conducta_frame = tk.LabelFrame(parent_frame, text="Conducta:", padx=10, pady=10)
        conducta_frame.pack(fill="x", padx=10, pady=5)

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
                self.entry_otros_rasgos = ScrolledText(conducta_frame, wrap=tk.WORD, width=40, height=4)
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

    def on_check_otros_rasgos(self):
        if self.otros_rasgos_var.get():
            self.entry_otros_rasgos.config(state=tk.NORMAL)
        else:
            self.entry_otros_rasgos.delete(0, tk.END)
            self.entry_otros_rasgos.config(state=tk.DISABLED)
    
    def get_behavior_values(self):
        return {
            "scared_to_go_to_school": self.miedo_escuela_var.get(),
            "enuresis": self.enuresis_var.get(),
            "nervous_tic": self.tic_nervioso_var.get(),
            "retraimiento": self.retraimiento_var.get(),
            "encopresis": self.encopresis_var.get(),
            "sadness": self.tristeza_var.get(),
            "aggression": self.agresividad_var.get(),
            "nail_biting": self.come_unas_var.get(),
            "frequent_crying": self.llantos_var.get(),
            "anxiety": self.andisedad_var.get(),
            "auto_aggression": self.auto_agresion_var.get(),
            "challenge_authority": self.reta_autoridad_var.get(),
            "irritability": self.irritabilidad_var.get(),
            "defiant": self.desafiante_var.get(),
            "impulsivity": self.impulsividad_var.get(),
            "other_behavioral_traits": self.otros_rasgos_var.get(),
            "other_behavioral_traits_text": self.entry_otros_rasgos.get()
        }