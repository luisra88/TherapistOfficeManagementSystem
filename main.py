import tkinter as tk
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title("Patient Management System")
    root.geometry("800x600")

    # Add simple label to the window
    label = tk.Label(root, text="Welcome to the Therapist Office Management System", font=("Arial", 16))
    label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()