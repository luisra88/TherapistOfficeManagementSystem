import tkinter as tk
from ..utils.patient_ui_utils import add_date_entry, add_field

class MainSection:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.widgets = {}
        self.create_main_section(parent_frame)

    def create_main_section(self, parent_frame):
        """Create the layout and widgets for the main section."""
        main_frame = tk.LabelFrame(parent_frame, text="Main Section", padx=10, pady=10)
        main_frame.pack(fill="x", padx=10, pady=5)

        # Configure grid layout
        for i in range(4):
            main_frame.grid_columnconfigure(i, weight=1 if i % 2 == 0 else 2)

        # Add all widgets with their labels
        add_field(main_frame, "Nombre con apellidos:", 0, 0, self.widgets, "full_name")
        add_field(main_frame, "Número de registro:", 0, 2, self.widgets, "registry_number")
        add_date_entry(main_frame, "Fecha de nacimiento:", 1, 0, self.widgets, "date_of_birth")
        add_field(main_frame, "Nombre de la madre:", 1, 2, self.widgets, "mothers_name")
        add_field(main_frame, "Nombre del padre:", 2, 0, self.widgets, "fathers_name")
        add_field(main_frame, "Nombre del encargado:", 2, 2, self.widgets, "guardian_name")
        add_field(main_frame, "Dirección:", 3, 0, self.widgets, "address")
        add_field(main_frame, "Teléfono:", 3, 2, self.widgets, "phone")
        add_field(main_frame, "Email:", 4, 0, self.widgets, "email")
        add_field(main_frame, "Persona que refiere:", 5, 0, self.widgets, "referal_from")
        add_field(main_frame, "Puesto:", 5, 2, self.widgets, "post")

    def get_values(self):
        """Extract and return values from all widgets."""
        return {name: widget.get() for name, widget in self.widgets.items()}

