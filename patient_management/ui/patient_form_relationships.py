import tkinter as tk
from tkinter import ttk
class PersonalRelationships:
    def __init__(self, parent_frame):
        """Initialize and create the main section with all fields."""
        self.create_personal_relationships_section(parent_frame)
    def create_personal_relationships_section(self, parent_frame):
        self.relaciones_interpersonales_frame = tk.LabelFrame(parent_frame, text="Relaciones interpersonales:", padx=10, pady=10)
        self.relaciones_interpersonales_frame.pack(fill="x", padx=10, pady=5)

        ri_combo_options = ["Adecuada", "No adecuada", "N/A"]
        tk.Label(self.relaciones_interpersonales_frame, text="Relaciones con sus padres o encargados").grid(row=0, column=0, columnspan=2, sticky="w")
        self.relaciones_padres_combo = ttk.Combobox(self.relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_padres_combo.grid(row=0, column=2, sticky="w")
        self.relaciones_padres_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(self.relaciones_interpersonales_frame, text="Relaciones con sus hermanos").grid(row=1, column=0, columnspan=2, sticky="w")
        self.relaciones_hermanos_combo = ttk.Combobox(self.relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_hermanos_combo.grid(row=1, column=2, sticky="w")
        self.relaciones_hermanos_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(self.relaciones_interpersonales_frame, text="Relaciones con su grupo de pares").grid(row=2, column=0, columnspan=2, sticky="w")
        self.relaciones_grupo_combo = ttk.Combobox(self.relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_grupo_combo.grid(row=2, column=2, sticky="w")
        self.relaciones_grupo_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(self.relaciones_interpersonales_frame, text="Relaciones con los adultos").grid(row=3, column=0, columnspan=2, sticky="w")
        self.relaciones_adultos_combo = ttk.Combobox(self.relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_adultos_combo.grid(row=3, column=2, sticky="w")
        self.relaciones_adultos_combo.bind("<MouseWheel>", self.empty_scroll_command)
        tk.Label(self.relaciones_interpersonales_frame, text="Relaciones con figuras de autoridad").grid(row=4, column=0, columnspan=2, sticky="w")
        self.relaciones_autoridad_combo = ttk.Combobox(self.relaciones_interpersonales_frame, values=ri_combo_options, state="readonly")
        self.relaciones_autoridad_combo.grid(row=4, column=2, sticky="w")
        self.relaciones_autoridad_combo.bind("<MouseWheel>", self.empty_scroll_command)

    def empty_scroll_command(self, event):
        """Pass scroll event to the parent frame."""
        self.relaciones_interpersonales_frame.master.event_generate("<MouseWheel>", delta=event.delta)
        return "break"
    
    def get_relationships_values(self):
        return {
            "father_or_guardian_relationship": self.relaciones_padres_combo.get(),
            "sibling_relationship": self.relaciones_hermanos_combo.get(),
            "peer_group_relationship": self.relaciones_grupo_combo.get(),
            "adult_relationship": self.relaciones_adultos_combo.get(),
            "authority_relationship": self.relaciones_autoridad_combo.get(),
        }