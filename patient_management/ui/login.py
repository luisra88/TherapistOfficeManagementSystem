import tkinter as tk
from tkinter import messagebox
from patient_management.utils.user_auth import authenticate_user
import logging
from ..utils.logging_config import setup_logging
from ..ui.home import Home

# Call this early on
setup_logging()
logger = logging.getLogger(__name__)

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")

        self.label_username = tk.Label(root, text="Username:")
        self.label_username.pack(pady=10)
        self.entry_username = tk.Entry(root)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.pack(pady=10)
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(root, text="Login", command=self.login)
        self.button_login.pack(pady=20)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if authenticate_user(username, password):
            logger.info("Login", "Login successful")
            self.root.destroy()  # Close login window
            self.open_home()
        else:
            messagebox.showerror("Login: %s", "Invalid username or password")
    
    def open_home(self):
        """Open the Home UI."""
        home_root = tk.Tk()  # Create a new Tkinter window for Home
        home_instance = Home(home_root)      # Initialize the Home UI
        home_root.mainloop()  # Start the main loop for the Home UI

if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()