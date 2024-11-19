import tkinter as tk
from ..utils.patient_ui_utils import add_field

class ScholarInfo:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.widgets = {}
        self.create_scholar_info_section(parent_frame)

    def create_scholar_info_section(self, parent_frame):
        scholar_frame = tk.LabelFrame(parent_frame, text="Historial Escolar", padx=10, pady=10)
        scholar_frame.pack(fill="x", padx=10, pady=5)


        # School
        add_field(scholar_frame, "Escuela:", 0, 0, self.widgets, "school_name")
        # Education region
        add_field(scholar_frame, "Región educativa:", 0, 2, self.widgets, "education_region")
        # Municipality
        add_field(scholar_frame, "Municipio:", 1, 0, self.widgets, "municipality")
        # District
        add_field(scholar_frame, "Distrito:", 1, 2, self.widgets, "district")
        # Grade/group
        add_field(scholar_frame, "Grado/Grupo:", 2, 0, self.widgets, "grade_group")

    
    def get_values(self):
        """Extract and return values from all widgets."""
        return {name: widget.get() for name, widget in self.widgets.items()}