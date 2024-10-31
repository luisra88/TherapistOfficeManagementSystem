import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date

class Treatments:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.create_treatment_section(parent_frame)
    def create_treatment_section(self, parent_frame):
        self.treatment_frame = tk.LabelFrame(parent_frame, text="Tratamiento:", padx=10, pady=10)
        self.treatment_frame.pack(fill="x", padx=10, pady=5)

        #Tratamientos
        tk.Label(self.treatment_frame, text="Disciplina").grid(row=0, column=0, sticky="w")
        tk.Label(self.treatment_frame, text="Frecuencia").grid(row=0, column=1, sticky="w")
        tk.Label(self.treatment_frame, text="Duración").grid(row=0, column=2, sticky="w")
        tk.Label(self.treatment_frame, text="Modalidad").grid(row=0, column=3, sticky="w")
        tk.Label(self.treatment_frame, text="Fecha de Inicio").grid(row=0, column=4, sticky="w")
        tk.Label(self.treatment_frame, text="Estatus").grid(row=0, column=5, sticky="w")

        self.regular_treatments = []
        self.habla_var = tk.BooleanVar()
        tk.Checkbutton(self.treatment_frame, text="Habla-Lenguaje", variable=self.habla_var, command=self.on_check_habla).grid(row=1, column=0, sticky="w")
        self.habla_frequency_combo = ttk.Combobox(self.treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.habla_frequency_combo.grid(row=1, column=1)
        self.habla_frequency_combo.config(state="disabled")
        self.habla_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.habla_duration_combo = ttk.Combobox(self.treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.habla_duration_combo.grid(row=1, column=2)
        self.habla_duration_combo.config(state="disabled")
        self.habla_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.habla_modalidad_combo = ttk.Combobox(self.treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.habla_modalidad_combo.grid(row=1, column=3)
        self.habla_modalidad_combo.config(state="disabled")
        self.habla_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_habla = DateEntry(self.treatment_frame, date_pattern='yyyy-mm-dd', showweeknumbers=False, maxdate=date.today())
        self.entry_habla.grid(row=1, column=4)
        self.entry_habla.config(state="disabled")
        self.habla_status_combo = ttk.Combobox(self.treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.habla_status_combo.grid(row=1, column=5)
        self.habla_status_combo.config(state="disabled")
        self.habla_status_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.regular_treatments.append((self.habla_var, "Habla-Lenguaje", self.habla_frequency_combo, self.habla_duration_combo, self.habla_modalidad_combo, self.entry_habla, self.habla_status_combo))

        self.ocupacional_var = tk.BooleanVar()
        tk.Checkbutton(self.treatment_frame, text="Ocupacional", variable=self.ocupacional_var, command=self.on_check_ocupacional).grid(row=2, column=0, sticky="w")
        self.ocupacional_frequency_combo = ttk.Combobox(self.treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.ocupacional_frequency_combo.grid(row=2, column=1)
        self.ocupacional_frequency_combo.config(state="disabled")
        self.ocupacional_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.ocupacional_duration_combo = ttk.Combobox(self.treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.ocupacional_duration_combo.grid(row=2, column=2)
        self.ocupacional_duration_combo.config(state="disabled")
        self.ocupacional_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.ocupacional_modalidad_combo = ttk.Combobox(self.treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.ocupacional_modalidad_combo.grid(row=2, column=3)
        self.ocupacional_modalidad_combo.config(state="disabled")
        self.ocupacional_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_ocupacional = DateEntry(self.treatment_frame, date_pattern='yyyy-mm-dd', showweeknumbers=False, maxdate=date.today())
        self.entry_ocupacional.grid(row=2, column=4)
        self.entry_ocupacional.config(state="disabled")
        self.ocupacional_status_combo = ttk.Combobox(self.treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.ocupacional_status_combo.grid(row=2, column=5)
        self.ocupacional_status_combo.config(state="disabled")
        self.ocupacional_status_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.regular_treatments.append((self.ocupacional_var, "Ocupacional", self.ocupacional_frequency_combo, self.ocupacional_duration_combo, self.ocupacional_modalidad_combo, self.entry_ocupacional, self.ocupacional_status_combo))

        self.psicologica_var = tk.BooleanVar()
        tk.Checkbutton(self.treatment_frame, text="Psicológica", variable=self.psicologica_var, command=self.on_check_psicologica).grid(row=3, column=0, sticky="w")
        self.psicologica_frequency_combo = ttk.Combobox(self.treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.psicologica_frequency_combo.grid(row=3, column=1)
        self.psicologica_frequency_combo.config(state="disabled")
        self.psicologica_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.psicologica_duration_combo = ttk.Combobox(self.treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.psicologica_duration_combo.grid(row=3, column=2)
        self.psicologica_duration_combo.config(state="disabled")
        self.psicologica_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.psicologica_modalidad_combo = ttk.Combobox(self.treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.psicologica_modalidad_combo.grid(row=3, column=3)
        self.psicologica_modalidad_combo.config(state="disabled")
        self.psicologica_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_psicologica = DateEntry(self.treatment_frame, date_pattern='yyyy-mm-dd', showweeknumbers=False, maxdate=date.today())
        self.entry_psicologica.grid(row=3, column=4)
        self.entry_psicologica.config(state="disabled")
        self.psicologica_status_combo = ttk.Combobox(self.treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.psicologica_status_combo.grid(row=3, column=5)
        self.psicologica_status_combo.config(state="disabled")
        self.psicologica_status_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.regular_treatments.append((self.psicologica_var, "Psicológica", self.psicologica_frequency_combo, self.psicologica_duration_combo, self.psicologica_modalidad_combo, self.entry_psicologica, self.psicologica_status_combo))

        self.fisica_var = tk.BooleanVar()
        tk.Checkbutton(self.treatment_frame, text="Física", variable=self.fisica_var, command=self.on_check_fisica).grid(row=4, column=0, sticky="w")
        self.fisica_frequency_combo = ttk.Combobox(self.treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.fisica_frequency_combo.grid(row=4, column=1)
        self.fisica_frequency_combo.config(state="disabled")
        self.fisica_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.fisica_duration_combo = ttk.Combobox(self.treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.fisica_duration_combo.grid(row=4, column=2)
        self.fisica_duration_combo.config(state="disabled")
        self.fisica_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.fisica_modalidad_combo = ttk.Combobox(self.treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.fisica_modalidad_combo.grid(row=4, column=3)
        self.fisica_modalidad_combo.config(state="disabled")
        self.fisica_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_fisica = DateEntry(self.treatment_frame, date_pattern='yyyy-mm-dd', showweeknumbers=False, maxdate=date.today())
        self.entry_fisica.grid(row=4, column=4)
        self.entry_fisica.config(state="disabled")
        self.fisica_status_combo = ttk.Combobox(self.treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.fisica_status_combo.grid(row=4, column=5)
        self.fisica_status_combo.config(state="disabled")
        self.fisica_status_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.regular_treatments.append((self.fisica_var, "Física", self.fisica_frequency_combo, self.fisica_duration_combo, self.fisica_modalidad_combo, self.entry_fisica, self.fisica_status_combo))

        self.psicquiatrica_var = tk.BooleanVar()
        tk.Checkbutton(self.treatment_frame, text="Psicquiátrica", variable=self.psicquiatrica_var, command=self.on_check_psicquiatrica).grid(row=5, column=0, sticky="w")
        self.psicquiatrica_frequency_combo = ttk.Combobox(self.treatment_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        self.psicquiatrica_frequency_combo.grid(row=5, column=1)
        self.psicquiatrica_frequency_combo.config(state="disabled")
        self.psicquiatrica_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.psicquiatrica_duration_combo = ttk.Combobox(self.treatment_frame, values=["30 min", "45 min"], state="readonly")
        self.psicquiatrica_duration_combo.grid(row=5, column=2)
        self.psicquiatrica_duration_combo.config(state="disabled")
        self.psicquiatrica_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.psicquiatrica_modalidad_combo = ttk.Combobox(self.treatment_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        self.psicquiatrica_modalidad_combo.grid(row=5, column=3)
        self.psicquiatrica_modalidad_combo.config(state="disabled")
        self.psicquiatrica_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.entry_psicquiatrica = DateEntry(self.treatment_frame, date_pattern='yyyy-mm-dd', showweeknumbers=False, maxdate=date.today())
        self.entry_psicquiatrica.grid(row=5, column=4)
        self.entry_psicquiatrica.config(state="disabled")
        self.psicquiatrica_status_combo = ttk.Combobox(self.treatment_frame, values=["Alta", "Baja"], state="readonly")
        self.psicquiatrica_status_combo.grid(row=5, column=5)
        self.psicquiatrica_status_combo.config(state="disabled")
        self.psicquiatrica_status_combo.bind("<MouseWheel>", self.empty_scroll_command)
        self.regular_treatments.append((self.psicquiatrica_var, "Psicquiátrica", self.psicquiatrica_frequency_combo, self.psicquiatrica_duration_combo, self.psicquiatrica_modalidad_combo, self.entry_psicquiatrica, self.psicquiatrica_status_combo))

        self.otra_disciplina_var = tk.BooleanVar()
        self.otras_disciplinas = []
        tk.Checkbutton(self.treatment_frame, text="Otra:", variable=self.otra_disciplina_var, command=self.on_check_otra_disciplina).grid(row=6, column=0, sticky="w")
        self.add_other_treatment_button = tk.Button(self.treatment_frame, text="Añadir otra disciplina", command=self.add_otra_disciplina)
        self.add_other_treatment_button.grid(row=6, column=1)
        self.add_other_treatment_button.config(state="disabled")

    def empty_scroll_command(self, event):
        """Pass scroll event to the parent frame."""
        self.treatment_frame.master.event_generate("<MouseWheel>", delta=event.delta)
        return "break" 
    
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

    def on_check_otra_disciplina(self):
        if self.otra_disciplina_var.get():
            self.otras_disciplinas_frame = tk.Frame(self.treatment_frame)
            self.otras_disciplinas_frame.grid(row=7, column=0, columnspan=6, sticky="w")
            self.add_otra_disciplina()
            self.add_other_treatment_button.config(state="normal")
        else:
            self.clear_otras_disciplinas()
            self.add_other_treatment_button.config(state="disabled")
            self.otras_disciplinas_frame.destroy()
    

    def add_otra_disciplina(self):
        row = len(self.otras_disciplinas)
        entry_otra_disciplina = ttk.Entry(self.otras_disciplinas_frame)
        entry_otra_disciplina.grid(row=row, column=0)
        otra_disciplina_frequency_combo = ttk.Combobox(self.otras_disciplinas_frame, values=["1x semanal", "2x semanal", "3x semanal", "4x semanal"], state="readonly")
        otra_disciplina_frequency_combo.grid(row=row, column=1)
        otra_disciplina_frequency_combo.bind("<MouseWheel>", self.empty_scroll_command)
        otra_disciplina_duration_combo = ttk.Combobox(self.otras_disciplinas_frame, values=["30 min", "45 min"], state="readonly")
        otra_disciplina_duration_combo.grid(row=row, column=2)
        otra_disciplina_duration_combo.bind("<MouseWheel>", self.empty_scroll_command)
        otra_disciplina_modalidad_combo = ttk.Combobox(self.otras_disciplinas_frame, values=["Individual", "Grupal", "Otra"], state="readonly")
        otra_disciplina_modalidad_combo.grid(row=row, column=3)
        otra_disciplina_modalidad_combo.bind("<MouseWheel>", self.empty_scroll_command)
        otra_disciplina_fisica = DateEntry(self.otras_disciplinas_frame, date_pattern='yyyy-mm-dd', showweeknumbers=False, maxdate=date.today())
        otra_disciplina_fisica.grid(row=row, column=4)
        otra_disciplina_status_combo = ttk.Combobox(self.otras_disciplinas_frame, values=["Alta", "Baja"], state="readonly")
        otra_disciplina_status_combo.grid(row=row, column=5)
        otra_disciplina_status_combo.bind("<MouseWheel>", self.empty_scroll_command)

        self.otras_disciplinas.append((entry_otra_disciplina, otra_disciplina_frequency_combo, otra_disciplina_duration_combo, otra_disciplina_modalidad_combo, otra_disciplina_fisica, otra_disciplina_status_combo))
     
    def get_treatment_values(self):
        """Returns a list of tuples with the grade and times repeated values."""
        all_treatment_values = {}
        for var, type, frequency_combo, duration_combo, modalidad_combo, date, status_combo in self.regular_treatments:
            if var.get():
                treatment = {
                "treatment_type": type,
                "weekly_frequency": frequency_combo.get(),
                "duration": duration_combo.get(),
                "modality": modalidad_combo.get(),
                "start_date": date.get(),
                "status": status_combo.get()
                }
                all_treatment_values[type + "_treatment"] = treatment

        for type, frequency_combo, duration_combo, modalidad_combo, date, status_combo in self.otras_disciplinas:
            treatment = {
            "treatment_type": type.get(),
            "weekly_frequency": frequency_combo.get(),
            "duration": duration_combo.get(),
            "modality": modalidad_combo.get(),
            "start_date": date.get(),
            "status": status_combo.get()
        }
            all_treatment_values[type.get() + "_treatment"] = treatment
        return all_treatment_values
    
    def clear_otras_disciplinas(self):
        for widget in self.otras_disciplinas_frame.winfo_children():
            widget.destroy()
        self.otras_disciplinas.clear()