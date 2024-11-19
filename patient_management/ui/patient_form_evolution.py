import tkinter as tk
from tkinter import ttk

class EvolutionHistorySection:
    def __init__(self, parent_frame):
        # Frame setup
        self.evo_history_frame = tk.LabelFrame(parent_frame, text="Historial del desarrollo evolutivo", padx=10, pady=10)
        self.evo_history_frame.pack(fill="x", padx=10, pady=5)

        # History Origin - Dropdown selection
        tk.Label(self.evo_history_frame, text="Historial del desarrollo evolutivo surge de:").grid(row=0, column=0, sticky="w")
        self.history_origin = ttk.Combobox(self.evo_history_frame, values=["entrevista", "lectura de expediente"], state="readonly")
        self.history_origin.grid(row=0, column=1)
        self.history_origin.bind("<MouseWheel>", self.empty_scroll_command)

        # Variables for family members
        self.mama_var = tk.BooleanVar()
        self.papa_var = tk.BooleanVar()
        self.hermanos_var = tk.BooleanVar()
        self.abuelos_var = tk.BooleanVar()
        self.otros_var = tk.BooleanVar()

        # Create checkbuttons
        family_members = {
            "Mamá": self.mama_var,
            "Papá": self.papa_var,
            "Hermanos": self.hermanos_var,
            "Abuelos": self.abuelos_var,
            "Otros:": self.otros_var,
        }

        # Place checkbuttons in the frame
        fam_member_col = 0
        for member, var in family_members.items():
            if member == "Otros:":
                tk.Checkbutton(self.evo_history_frame, text=member, variable=var, command=self.on_otros_check).grid(row=2, column=fam_member_col, sticky="w")
            else:
                tk.Checkbutton(self.evo_history_frame, text=member, variable=var).grid(row=2, column=fam_member_col, sticky="w")
            fam_member_col += 1

        # Entry for specifying "Otros"
        self.entry_people_at_home = tk.Entry(self.evo_history_frame)
        self.entry_people_at_home.grid(row=2, column=5)
        self.entry_people_at_home.config(state="disabled")

        # Problems at home
        self.problems_at_home_var = tk.BooleanVar()
        tk.Checkbutton(self.evo_history_frame, text="Problemas en el hogar:", variable=self.problems_at_home_var, command=self.on_check_problems_at_home).grid(row=3, column=0, sticky="w")
        self.entry_problems_at_home = tk.Entry(self.evo_history_frame)
        self.entry_problems_at_home.grid(row=3, column=1)
        self.entry_problems_at_home.config(state="disabled")

    def on_otros_check(self):
        """Enable or disable the entry field based on the 'Otros' checkbox."""
        if self.otros_var.get():
            self.entry_people_at_home.config(state="normal")
        else:
            self.entry_people_at_home.delete(0, tk.END)
            self.entry_people_at_home.config(state="disabled")


    def on_check_problems_at_home(self):
        if self.problems_at_home_var.get():
            self.entry_problems_at_home.config(state="normal")
        else:
            self.entry_problems_at_home.delete(0, tk.END)
            self.entry_problems_at_home.config(state="disabled")

    def empty_scroll_command(self, event):
        """Pass scroll event to the parent frame."""
        self.evo_history_frame.master.event_generate("<MouseWheel>", delta=event.delta)
        return "break"
    
    def get_values(self):
        """Retrieve values from the section widgets."""
        values = {
            "evo_history_origin": self.history_origin.get(),
            "mom_at_home": self.mama_var.get(),
            "dad_at_home": self.papa_var.get(),
            "siblings_at_home": self.hermanos_var.get(),
            "grandparents_at_home": self.abuelos_var.get(),
            "other_at_home": self.otros_var.get(),
            "other_at_home_text": self.entry_people_at_home.get() if self.otros_var.get() else "",
            "problems_at_home": self.problems_at_home_var.get(),
            "problems_at_home_text": self.entry_problems_at_home.get() if self.problems_at_home_var.get() else "",
        }
        return values