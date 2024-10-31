import tkinter as tk
from tkinter import ttk

class ScholarHistory:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.create_historial_escolar_section(parent_frame)
    def create_historial_escolar_section(self, parent_frame):
        self.historial_escolar_frame = tk.LabelFrame(parent_frame, text="Historial escolar:", padx=10, pady=10)
        self.historial_escolar_frame.pack(fill="x", padx=10, pady=5)

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
        self.salon_completo_var = tk.BooleanVar()
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
        self.salon_completo_checkbox = tk.Checkbutton(self.historial_escolar_frame, text="Salón a tiempo completo", variable=self.salon_completo_var)
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
        #TODO: add code to make sure only a certain amount of entries can be added (1 for each grade)
        row = len(self.flunked_entries)
        all_grades = ('Pre-K', 'Kindergarten', '1er Grado', '2do Grado', '3er Grado', '4to Grado', '5to Grado', '6to Grado', '7mo Grado', '8vo Grado', '9no Grado', '10mo Grado', '11mo Grado', '12mo Grado')

        # Grade entry
        grade_label = tk.Label(self.flunked_entries_frame, text=f"Grado {row + 1}:")
        grade_label.grid(row=row, column=0, sticky="w")
        grade_combo = ttk.Combobox(self.flunked_entries_frame, values= all_grades, state="readonly")
        grade_combo.bind("<MouseWheel>", self.empty_scroll_command)
        grade_combo.grid(row=row, column=1, sticky="w")

        # Times repeated entry
        times_label = tk.Label(self.flunked_entries_frame, text="Veces:")
        times_label.grid(row=row, column=2, sticky="w")
        times_entry = tk.Entry(self.flunked_entries_frame, width=5)
        #TODO:need to create function to make sure only an integer can be entered into this entry
        times_entry.grid(row=row, column=3, sticky="w")

        # Store the entries to access them later if needed
        self.flunked_entries.append((grade_combo, times_entry))
    
    def clear_flunked_entries(self):
        """Clears all widgets within the flunked entries frame."""
        for widget in self.flunked_entries_frame.winfo_children():
            widget.destroy()
        self.flunked_entries.clear()

    def get_flunked_grades(self):
        """Returns a list of tuples with the grade and times repeated values."""
        flunked_values = []
        for grade_combo, times_entry in self.flunked_entries:
            grade = grade_combo.get()
            times = times_entry.get()
            if grade and times.isdigit():  # Ensure times is a valid integer
                flunked_values.append({
                "grade": grade,
                "times_failed": int(times)
            })
        return flunked_values

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
            self.salon_completo_var.set(tk.FALSE)
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
    
    def empty_scroll_command(self, event):
        """Pass scroll event to the parent frame."""
        self.historial_escolar_frame.master.event_generate("<MouseWheel>", delta=event.delta)
        return "break"
    
    def get_scholar_history_values(self):
        return {
            "head_start": self.head_start_var.get(),
            "kindergarten": self.kinderkarten_var.get(),
            "other_programs": self.otro_programa_var.get(),
            "other_programs_text": self.entry_otro_programa.get(),
            "held_back": self.flunked_var.get(),
            "academic_performance": self.ayuda_educacion_var.get(),
            "special_ed_salon_recurso": self.salon_recurso_var.get(),
            "special_ed_salon_fulltime": self.salon_completo_var.get(),
            "special_ed_other": self.otra_ayuda_var.get(),
            "special_ed_other_text": self.entry_otra_ayuda.get(),
            "current_academic_performance": self.entry_funcionamiento_academico.get()
        }
    
    def get_academic_difficulties_values(self):
        return {
            "reading_difficulty": self.lectura_var.get(),
            "writing_difficulty": self.escritura_var.get(),
            "math_difficulty": self.matematica_var.get(),
            "reading_comprehension_difficulty": self.comprension_var.get(),
            "inverts_substitutes_reading_difficulty": self.invierte_lectura_var.get(),
            "omits_reading_difficulty": self.omite_lectura_var.get(),
            "copy_writing_difficulty": self.copiar_var.get(),
            "inverts_substitutes_writing_difficulty": self.invierte_escritura_var.get(),
            "omits_writing_difficulty": self.omite_escritura_var.get(),
            "sum_substraction_math_difficulty": self.suma_var.get(),
            "multiplication_math_difficulty": self.multiplicacion_var.get(),
            "division_math_difficulty": self.division_var.get(),
            "other_difficulties": self.otras_dificultades_var.get(),
            "other_difficulties_text": self.entry_otras_dificultades.get(),

        }