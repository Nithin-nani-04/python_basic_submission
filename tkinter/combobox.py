import tkinter as tk
from tkinter import ttk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Combobox Example")
root.geometry("300x250")


# ---------------- FUNCTION TO SHOW SELECTION ----------------
def show_choice(event=None):
    """
    This function runs when the user selects an item from the combobox.
    The 'event' parameter is needed because we bind a selection event.
    """
    selected = combo.get()  # get selected value
    result_label.config(text=f"Selected: {selected}")


# ---------------- LABEL ----------------
label = tk.Label(root, text="Select a Programming Language:")
label.pack(pady=10)


# ---------------- COMBOBOX ----------------
# ttk.Combobox(root, values=[list of options])
combo = ttk.Combobox(root,
                     values=["Python", "Java", "C++", "JavaScript", "Go", "Rust"],
                     state="readonly")  
# state="readonly" stops the user from typing other values

combo.pack(pady=10)

# Set default selected value (optional)
combo.set("Python")

# Bind selection event
combo.bind("<<ComboboxSelected>>", show_choice)


# ---------------- LABEL TO DISPLAY CHOICE ----------------
result_label = tk.Label(root, text="Selected: Python")
result_label.pack(pady=20)


# ---------------- RUN APP ----------------
root.mainloop()
