import tkinter as tk

class EiwnEvaluationPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Resultados de Escala de Inteligencia Wechsler para Niños-R-PR (EIWN-R PR) ", font=("Arial", 14)).pack(pady=10)
        #TODO: Add real input fields for this evaluation method
    
    def get_data(self):
        """Return the data entered in this panel."""
        #TODO:Implement
        return