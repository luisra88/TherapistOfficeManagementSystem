import tkinter as tk
from tkinter import messagebox
from patient_management.utils.user_auth import authenticate_user

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
            messagebox.showinfo("Login", "Login successful")
            self.root.destroy()  # Close login window
        else:
            messagebox.showerror("Login", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()