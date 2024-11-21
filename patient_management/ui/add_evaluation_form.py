import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .execute_evaluation_form import ExecuteEvaluationForm

class AddEvaluationForm(tk.Toplevel):
    def __init__(self, parent, patient_name):
        super().__init__(parent)
        self.title("Add evaluation for " + patient_name)

         # Set the window size to the screen size
        screen_width = 1000
        screen_height = 700
        self.geometry(f"{screen_width}x{screen_height}")

         # Create a frame to hold everything inside a canvas for scrollability
        self.canvas = tk.Canvas(self, highlightthickness=0, bd=0)  # Remove focus/border indication
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Add a scrollbar to the canvas
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

         # Bind the mouse wheel to scroll the canvas
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows

        # Create an inner frame to hold all the form sections
        self.inner_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        self.inner_frame.bind("<Configure>", self.on_frame_configure)

        #add form sections
        self.create_metodos_evaluativos_section()
        self.create_conducta_observada_section()
        
        # Submit button
        self.button_start_evaluation = tk.Button(self, text="Start Evaluation", command=self.start_evaluation)
        self.button_start_evaluation.pack(pady=10)

        # Cancel button to close the window
        self.button_cancel = tk.Button(self, text="Cancel", command=self.close_window)
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

    def close_window(self):
        """Properly close the Toplevel window and re-enable the main window."""
        self.parent.grab_release()
        self.parent.attributes('-disabled', False)
        self.destroy()

    def start_evaluation(self):
        """Start the evaluation by opening ExecuteEvaluationForm."""
        selected_methods = self.get_selected_methods()
        if not selected_methods:
            messagebox.showinfo("No Methods Selected", "Please select at least one evaluation method.")
            return

        # Open the ExecuteEvaluationForm
        ExecuteEvaluationForm(self, selected_methods, self.observaciones_entry, self.otros_metodos_entry, self.otras_observaciones_entry)

    def create_metodos_evaluativos_section(self):
        metodos_evaluativos_frame = tk.LabelFrame(self.inner_frame,text="Métodos evaluativos", padx=10, pady=10)
        metodos_evaluativos_frame.grid(row=0, column=0, sticky="nsew")
        metodos_evaluativos_frame.pack(fill="x", padx=10, pady=5)

        self.wppsi_var = tk.BooleanVar()
        self.eiwn_var = tk.BooleanVar()
        self.wisc_var = tk.BooleanVar()
        self.eiwa_pr_var = tk.BooleanVar()
        self.eiwa_III_var = tk.BooleanVar()
        self.stanford_binet_var = tk.BooleanVar()
        self.toni_var = tk.BooleanVar()
        self.leiter_var = tk.BooleanVar()
        self.vineland_var = tk.BooleanVar()
        self.berry_var = tk.BooleanVar()
        self.bender_var = tk.BooleanVar()
        self.woodcock_var = tk.BooleanVar()
        self.boehm_var = tk.BooleanVar()
        self.matrices_raven_var = tk.BooleanVar()
        self.raven_ninos_var = tk.BooleanVar()
        self.raven_adultos_var = tk.BooleanVar()
        self.gars_var = tk.BooleanVar()
        self.figura_humana_var = tk.BooleanVar()
        self.dibujo_kinetico_var = tk.BooleanVar()
        self.oraciones_var = tk.BooleanVar()
        self.cara_arbol_persona_var = tk.BooleanVar()
        self.cat_tat_var = tk.BooleanVar()
        self.dovacs_var = tk.BooleanVar()
        self.adhd_rating_var = tk.BooleanVar()
        self.cuestionario_var = tk.BooleanVar()
        self.revision_var = tk.BooleanVar()
        self.observaciones_var = tk.BooleanVar()
        self.entrevista_var = tk.BooleanVar()
        self.otros_metodos_var = tk.BooleanVar()

        self.metodos_evaluativos = {
            "Escala de Inteligencia Wechsler para Preescolares (WPPSI-III)": self.wppsi_var,
            "Escala de Inteligencia Wechsler para Niños-R-PR (EIWN-R PR)": self.eiwn_var,
            "Escala de Inteligencia Wechsler para Niños (WISC-V Spanish)": self.wisc_var,
            "Escala de Inteligencia Wechsler para Adultos-PR (EIWA-PR)": self.eiwa_pr_var,
            "Escala de Inteligencia Wechsler para Adultos (EIWA-III)": self.eiwa_III_var,
            "Escala de Inteligencia Stanford-Binet (5ta ed.)": self.stanford_binet_var,
            "Prueba de Inteligencia No Verbal (TONI)": self.toni_var,
            "Leiter International Performance Scale-No Verbal-3": self.leiter_var,
            "Escala Madurez Social Vineland 3": self.vineland_var,
            "Prueba de Integración Visomotora Berry (6 ta ed.)": self.berry_var,
            "Prueba Percepción Visomotora Bender-Gestalt II": self.bender_var,
            "Batería IV, Woodcock-Muñoz": self.woodcock_var,
            "Prueba Conceptos Básicos Boehm": self.boehm_var,
            "Prueba de Matrices Progresivas Raven para": self.matrices_raven_var,
            "Niños": self.raven_ninos_var,
            "Adultos": self.raven_adultos_var,
            "Escala de Clasificación Gilliam Autismo-GARS-3": self.gars_var,
            "Prueba del Dibujo de la Figura Humana": self.figura_humana_var,
            "Prueba Dibujo Kinético de la Familia": self.dibujo_kinetico_var,
            "Prueba de Oraciones Incompletas": self.oraciones_var,
            "Prueba del Dibujo Casa-Árbol-Persona": self.cara_arbol_persona_var,
            "Prueba Apercepción Temática (CAT-TAT)": self.cat_tat_var,
            "Inventario de Depresión Kovacs-CDI": self.dovacs_var,
            "ADHD Rating Scale": self.adhd_rating_var,
            "Cuestionario de Problemas (Est./Padres)": self.cuestionario_var,
            "Revisión del expediente": self.revision_var,
            "Observaciones": self.observaciones_var,
            "Entrevista a:": self.entrevista_var,
            "Otros:": self.otros_metodos_var,
        }

        tk.Label(metodos_evaluativos_frame, text="Indique los métodos evaluativos utilizados en esta evaluacion").grid(row=0, column=0, columnspan=2, sticky="w")
        # Set weights for columns and rows
        for i in range(6):  # Assuming 6 columns (0 to 5)
            metodos_evaluativos_frame.columnconfigure(i, weight=1)
        row = 1
        column = 0
        for metodo, var in self.metodos_evaluativos.items():
            if metodo == "Prueba de Matrices Progresivas Raven para":
                ttk.Checkbutton(metodos_evaluativos_frame, text=metodo, variable=var, command=self.on_check_raven).grid(row=row, column=column, sticky="w")
            elif metodo == "Niños":
                self.ninos_checkbox = ttk.Checkbutton(metodos_evaluativos_frame, text=metodo, variable=var, command=self.on_check_ninos)
                self.ninos_checkbox.grid(row=row, column=column+1, sticky="w")
                self.ninos_checkbox.config(state=tk.DISABLED)
            elif metodo == "Adultos":
                self.adultos_checkbox = ttk.Checkbutton(metodos_evaluativos_frame, text=metodo, variable=var,command=self.on_check_adultos)
                self.adultos_checkbox.grid(row=row, column=column+2, sticky="w")
                self.adultos_checkbox.config(state=tk.DISABLED)
                row +=1
            elif metodo == "Observaciones":
                ttk.Checkbutton(metodos_evaluativos_frame, text=metodo, variable=var, command=self.on_check_observaciones).grid(row=row, column=column, sticky="w")
                self.observaciones_entry = tk.Entry(metodos_evaluativos_frame)
                self.observaciones_entry.grid(row=row, column=column+1, columnspan=3, sticky="ew")
                self.observaciones_entry.config(state=tk.DISABLED)
                row +=1
            elif metodo == "Entrevista a:":
                ttk.Checkbutton(metodos_evaluativos_frame, text=metodo, variable=var, command=self.on_check_entrevista).grid(row=row, column=column, sticky="w")
                self.entrevista_entry = tk.Entry(metodos_evaluativos_frame)
                self.entrevista_entry.grid(row=row, column=column+1, columnspan=3, sticky="ew")
                self.entrevista_entry.config(state=tk.DISABLED)
                row +=1
            elif metodo == "Otros:":
                ttk.Checkbutton(metodos_evaluativos_frame, text=metodo, variable=var, command=self.on_check_otros_metodos).grid(row=row, column=column, sticky="w")
                self.otros_metodos_entry = tk.Entry(metodos_evaluativos_frame)
                self.otros_metodos_entry.grid(row=row, column=column+1, columnspan=5, sticky="ew")
                self.otros_metodos_entry.config(state=tk.DISABLED)
                row +=1
            else:
                ttk.Checkbutton(metodos_evaluativos_frame, text=metodo, variable=var).grid(row=row, column=column, columnspan=2, sticky="w")
                row +=1
            if row >= 15:
                row = 1
                column = 3

    def create_conducta_observada_section(self):
        conducta_observada_frame = tk.LabelFrame(self.inner_frame, text="Conducta durante la evaluacion", padx=10, pady=10)
        conducta_observada_frame.pack(fill="x", padx=10, pady=5)
        # Example for setting the grid weights
        for i in range(6):  # Assume 6 columns in the frame
            conducta_observada_frame.columnconfigure(i, weight=1)
        for i in range(12):  # Assume 15 rows
            conducta_observada_frame.rowconfigure(i, weight=1)

        tk.Label(conducta_observada_frame, text="Conducta observada durante la evaluación:").grid(row=0, column=0, columnspan=2, sticky="w")

        tk.Label(conducta_observada_frame, text="Relación con el examinador").grid(row=1, column=0, sticky="w")
        self.relacion_examinador_combo = ttk.Combobox(conducta_observada_frame, values=["Positiva", "Pasiva", "Negativa", "Agresiva"], state="readonly")
        self.relacion_examinador_combo.grid(row=1, column=1, sticky="w")
        self.relacion_examinador_combo.bind("<MouseWheel>", self.checkbox_scroll)
        tk.Label(conducta_observada_frame, text="Dispocision").grid(row=2, column=0, sticky="w")
        self.disposicion_combo = ttk.Combobox(conducta_observada_frame, values=["Interesado", "Desinteresado"], state="readonly")
        self.disposicion_combo.grid(row=2, column=1, sticky="w")
        self.disposicion_combo.bind("<MouseWheel>", self.checkbox_scroll)
        tk.Label(conducta_observada_frame, text="Nivel de atención").grid(row=3, column=0, sticky="w")
        self.nivel_atencion_combo = ttk.Combobox(conducta_observada_frame, values=["Apropiada", "Disminuye gradualmente"], state="readonly")
        self.nivel_atencion_combo.grid(row=3, column=1, sticky="w")
        self.nivel_atencion_combo.bind("<MouseWheel>", self.checkbox_scroll)
        tk.Label(conducta_observada_frame, text="Nivel de actividad").grid(row=4, column=0, sticky="w")
        self.nivel_actividad_combo = ttk.Combobox(conducta_observada_frame, values=["Apropiada","Aumenta gradualmente", "Baja"])
        self.nivel_actividad_combo.grid(row=4, column=1, sticky="w")
        self.nivel_actividad_combo.bind("<MouseWheel>", self.checkbox_scroll)
        tk.Label(conducta_observada_frame, text="Nivel de ejecución ").grid(row=5, column=0, sticky="w")
        self.nivel_ejecucion_combo = ttk.Combobox(conducta_observada_frame, values=["Realiza las tareas en forma independiente y consistente", "Muestra interés e intenta realizar las tareas", "No logra realizar las tareas"], state="readonly")
        self.nivel_ejecucion_combo.grid(row=5,column=1, columnspan=2, sticky="ew")
        self.nivel_ejecucion_combo.bind("<MouseWheel>", self.checkbox_scroll)
        tk.Label(conducta_observada_frame, text="Conducta observada").grid(row=6, column=0, sticky="w")

        self.cooperador_var = tk.BooleanVar()
        self.organizado_var = tk.BooleanVar()
        self.motivado_var = tk.BooleanVar()
        self.rapido_var = tk.BooleanVar()
        self.impulsivo_var = tk.BooleanVar()
        self.negativo_var = tk.BooleanVar()
        self.descuidado_var = tk.BooleanVar()
        self.desorganizado_var = tk.BooleanVar()
        self.hostil_var = tk.BooleanVar()

        self.conductas = {
            "Cooperador": self.cooperador_var,
            "Organizado": self.organizado_var,
            "Motivado": self.motivado_var,
            "Trabaja rápido": self.rapido_var,
            "Impulsivo": self.impulsivo_var,
            "Negativo": self.negativo_var,
            "Descuidado": self.descuidado_var,
            "Desorganizado": self.desorganizado_var,
            "Hostil": self.hostil_var,
        }
        row = 7
        column = 0
        for conducta, var in self.conductas.items():
            tk.Checkbutton(conducta_observada_frame, text=conducta, variable=var).grid(row=row, column=column, sticky="w")
            if column >= 2:
                row +=1
                column = 0
            else:
                column += 1

        tk.Label(conducta_observada_frame, text="Lateralidad").grid(row=row, column=0, sticky="w")
        self.lateralidad_combo = ttk.Combobox(conducta_observada_frame, values=["Derecha", "Izquierda", "Ambidiestro"], state="readonly")
        self.lateralidad_combo.grid(row=row,column=1,sticky="w")
        self.lateralidad_combo.bind("<MouseWheel>", self.checkbox_scroll)
        tk.Label(conducta_observada_frame, text="Otras observaciones:").grid(row=row+1, column=0, sticky="w")
        self.otras_observaciones_entry = tk.Text(conducta_observada_frame, height=5, width=80)
        self.otras_observaciones_entry.grid(row=row+2, column=0, columnspan=2, sticky="nsew")
    
    def on_check_raven(self):
        if self.matrices_raven_var.get():
            self.ninos_checkbox.config(state=tk.NORMAL)
            self.adultos_checkbox.config(state=tk.NORMAL)
        else:
            self.raven_ninos_var.set(tk.FALSE)
            self.raven_adultos_var.set(tk.FALSE)
            self.ninos_checkbox.config(state=tk.DISABLED)
            self.adultos_checkbox.config(state=tk.DISABLED)

    def on_check_observaciones(self):
        if self.observaciones_var.get():
            self.observaciones_entry.config(state=tk.NORMAL)
        else:
            self.observaciones_entry.delete(0, tk.END)
            self.observaciones_entry.config(state=tk.DISABLED)

    def on_check_entrevista(self):
        if self.entrevista_var.get():
            self.entrevista_entry.config(state=tk.NORMAL)
        else:
            self.entrevista_entry.delete(0, tk.END)
            self.entrevista_entry.config(state=tk.DISABLED)

    def on_check_otros_metodos(self):
        if self.otros_metodos_var.get():
            self.otros_metodos_entry.config(state=tk.NORMAL)
        else:
            self.otros_metodos_entry.delete(0, tk.END)
            self.otros_metodos_entry.config(state=tk.DISABLED) 

    def on_check_ninos(self):
        if self.raven_ninos_var.get():
            self.raven_adultos_var.set(tk.FALSE)
    
    def on_check_adultos(self):
        if self.raven_adultos_var.get():
            self.raven_ninos_var.set(tk.FALSE)

    def checkbox_scroll(self, event):
        if event.num == 5 or event.delta == -120:  # Scroll down
            self.canvas.yview_scroll(1, "units")
        elif event.num == 4 or event.delta == 120:  # Scroll up
            self.canvas.yview_scroll(-1, "units")
        return "break"
    
    def get_selected_methods(self):
        """Return a list of selected evaluation methods."""
        selected_methods = []
        for method, var in self.metodos_evaluativos.items():
            if var.get() and method != "Prueba de Matrices Progresivas Raven para":  # Check if the checkbox is selected
                selected_methods.append(method)
        return selected_methods