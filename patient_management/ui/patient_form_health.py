
import tkinter as tk

class HealthHistory:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.create_health_history_section(parent_frame)

    def create_health_history_section(self, parent_frame):
        health_frame = tk.LabelFrame(parent_frame, text="Enfermedades", padx=10, pady=10)
        health_frame.pack(fill="x", padx=10, pady=5)

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
    
    def get_illnesses_values(self):
        return {
            "illness_asma": self.asma_bronquial_var.get(),
            "illness_pulmonia": self.pulmonia_var.get(),
            "illness_fiebres": self.fiebres_var.get(),
            "illness_seizures": self.convulsiones_enfermedades_var.get(),
            "illness_surgeries": self.cirugias_var.get(),
            "illness_diabetes": self.diabetes_var.get(),
            "illness_other_illnesses": self.other_illnesses_var.get(),
            "illness_other_illnesses_text": self.entry_other_illnesses.get(),
        }
    
    def on_check_other_illnesses(self):
        if self.other_illnesses_var.get():
            self.entry_other_illnesses.config(state="normal")
        else:
            self.entry_other_illnesses.delete(0, tk.END)
            self.entry_other_illnesses.config(state="disabled")
