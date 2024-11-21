import tkinter as tk
from tkinter import ttk
from .evaluation_forms.adhd_rating_evaluation_panel import AdhdEvaluationPanel
from .evaluation_forms.bender_evaluation_panel import BenderEvaluationPanel
from .evaluation_forms.berry_evaluation_panel import BerryEvaluationPanel
from .evaluation_forms.boehm_evaluation_panel import BoehmEvaluationPanel
from .evaluation_forms.cara_arbol_persona_evaluation_panel import CaraArbolPersonaEvaluationPanel
from .evaluation_forms.cat_tat_evaluation_panel import CatTatEvaluationPanel
from .evaluation_forms.cuestionario_evaluation_panel import CuestionarioEvaluationPanel
from .evaluation_forms.dibujo_kinetico_evaluation_panel import DibujoKineticoEvaluationPanel
from .evaluation_forms.dovacs_evaluation_panel import DovacsEvaluationPanel
from .evaluation_forms.eiwa_iii_evaluation_panel import EiwaIIIEvaluationPanel
from .evaluation_forms.eiwa_pr_evaluation_panel import EiwaPREvaluationPanel
from .evaluation_forms.eiwn_evaluation_panel import EiwnEvaluationPanel
from .evaluation_forms.entrevista_evaluation_panel import EntrevistaEvaluationPanel
from .evaluation_forms.figura_humana_evaluation_panel import FiguraHumanaEvaluationPanel
from .evaluation_forms.gars_evaluation_panel import GarsEvaluationPanel
from .evaluation_forms.leiter_evaluation_panel import LeiterEvaluationPanel
from .evaluation_forms.observaciones_evaluation_panel import ObservacionesEvaluationPanel
from .evaluation_forms.oraciones_evaluation_panel import OracionesEvaluationPanel
from .evaluation_forms.otros_metodos_evaluation_panel import OtrosMetodosEvaluationPanel
from .evaluation_forms.raven_adultos_evaluation_panel import RavenAdultosEvaluationPanel
from .evaluation_forms.raven_ninos_evaluation_panel import RavenNinosEvaluationPanel
from .evaluation_forms.revision_evaluation_panel import RevisionEvaluationPanel
from .evaluation_forms.stanford_evaluation_panel import StanfordEvaluationPanel
from .evaluation_forms.toni_evaluation_panel import ToniEvaluationPanel
from .evaluation_forms.vineland_evaluation_panel import VinelandEvaluationPanel
from .evaluation_forms.wisc_evaluation_panel import WiscEvaluationPanel
from .evaluation_forms.woodcock_evaluation_panel import WoodcockEvaluationPanel
from .evaluation_forms.wppsi_evaluation_panel import WppsiEvaluationPanel

PANEL_FACTORY = {
        "Escala de Inteligencia Wechsler para Preescolares (WPPSI-III)": WppsiEvaluationPanel,
        "Escala de Inteligencia Wechsler para Niños-R-PR (EIWN-R PR)": EiwnEvaluationPanel,
        "Escala de Inteligencia Wechsler para Niños (WISC-V Spanish)": WiscEvaluationPanel,
        "Escala de Inteligencia Wechsler para Adultos-PR (EIWA-PR)": EiwaPREvaluationPanel,
        "Escala de Inteligencia Wechsler para Adultos (EIWA-III)": EiwaIIIEvaluationPanel,
        "Escala de Inteligencia Stanford-Binet (5ta ed.)": StanfordEvaluationPanel,
        "Prueba de Inteligencia No Verbal (TONI)": ToniEvaluationPanel,
        "Leiter International Performance Scale-No Verbal-3": LeiterEvaluationPanel,
        "Escala Madurez Social Vineland 3": VinelandEvaluationPanel,
        "Prueba de Integración Visomotora Berry (6 ta ed.)": BerryEvaluationPanel,
        "Prueba Percepción Visomotora Bender-Gestalt II": BenderEvaluationPanel,
        "Batería IV, Woodcock-Muñoz": WoodcockEvaluationPanel,
        "Prueba Conceptos Básicos Boehm": BoehmEvaluationPanel,
        "Niños": RavenNinosEvaluationPanel,
        "Adultos": RavenAdultosEvaluationPanel,
        "Escala de Clasificación Gilliam Autismo-GARS-3": GarsEvaluationPanel,
        "Prueba del Dibujo de la Figura Humana": FiguraHumanaEvaluationPanel,
        "Prueba Dibujo Kinético de la Familia": DibujoKineticoEvaluationPanel,
        "Prueba de Oraciones Incompletas": OracionesEvaluationPanel,
        "Prueba del Dibujo Casa-Árbol-Persona": CaraArbolPersonaEvaluationPanel,
        "Prueba Apercepción Temática (CAT-TAT)": CatTatEvaluationPanel,
        "Inventario de Depresión Kovacs-CDI": DovacsEvaluationPanel,
        "ADHD Rating Scale": AdhdEvaluationPanel,
        "Cuestionario de Problemas (Est./Padres)": CuestionarioEvaluationPanel,
        "Revisión del expediente": RevisionEvaluationPanel,
        "Observaciones": ObservacionesEvaluationPanel,
        "Entrevista a:": EntrevistaEvaluationPanel,
        "Otros:": OtrosMetodosEvaluationPanel
}

class ExecuteEvaluationForm(tk.Toplevel):
    def __init__(self, parent, methods, observaciones_entry, entrevista_entry, otros_metodos_entry):
        super().__init__(parent)
        self.title("Execute Evaluation")
        self.methods = methods
        self.current_index = 0
        self.panels = {}  # To store the created panel instances
        self.results = {}  # To store the results from each panel

        self.holding_frame = tk.Frame(self)
        self.holding_frame.pack(fill="both", expand=True)

        # Navigation Buttons
        self.prev_button = tk.Button(self, text="Previous", command=self.prev_method)
        self.prev_button.pack(side="left", padx=5, pady=5)

        self.next_button = tk.Button(self, text="Next", command=self.next_method)
        self.next_button.pack(side="left", padx=5, pady=5)

        self.finish_button = tk.Button(self, text="Finish", command=self.finish_evaluation)
        self.finish_button.pack(side="right", padx=5, pady=5)

        # Display the first method's panel
        self.show_current_method()

    def load_panel(self, method):
        if method not in PANEL_FACTORY:
            tk.Label(self.holding_frame, text=f"Unknown method: {method}").pack()
            return None

        if method not in self.panels:
            try:
                panel_class = PANEL_FACTORY[method]
                self.panels[method] = panel_class(self.holding_frame)
            except Exception as e:
                tk.Label(self.holding_frame, text=f"Error creating panel for {method}: {e}").pack()
                return None
        return self.panels[method]

    def show_current_method(self):
        """Show the panel for the current method."""
        # Clear the frame
        for widget in self.holding_frame.winfo_children():
            widget.destroy()

        # Get the current method
        method = self.methods[self.current_index]
        # Ensure the current method panel is removed if destroyed
        if method in self.panels and not self.panels[method].winfo_exists():
            del self.panels[method]

        # Load and pack the panel
        panel = self.load_panel(method)
        if panel:
            panel.pack(fill="both", expand=True)

        # Update navigation buttons
        self.prev_button.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_index < len(self.methods) - 1 else tk.DISABLED)


    def next_method(self):
        """Go to the next method."""
        self.current_index += 1
        self.show_current_method()

    def prev_method(self):
        """Go to the previous method."""
        self.current_index -= 1
        self.show_current_method()

    def finish_evaluation(self):
        """Handle finish button click."""
        results = {}
        # Process results (e.g., save to database or display confirmation)
        print(results)  # Replace with actual processing
        self.destroy()
