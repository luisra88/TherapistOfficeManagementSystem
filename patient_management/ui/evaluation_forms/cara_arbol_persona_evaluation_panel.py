import tkinter as tk

class CaraArbolPersonaEvaluationPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Resultados de Prueba del Dibujo Casa-Árbol-Persona", font=("Arial", 14)).pack(pady=10)
        #TODO: Add real input fields for this evaluation method
    
    def get_data(self):
        """Return the data entered in this panel."""
        #TODO:Implement
        return