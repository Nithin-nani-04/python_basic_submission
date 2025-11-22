import tkinter as tk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("300x250")


# ---------------- VARIABLE ----------------
# Radiobuttons must share the SAME variable.
# Only one Radiobutton can be selected at a time.
selected_language = tk.StringVar()
selected_language.set("")    # default empty or you can set a default value


# ---------------- FUNCTIONS ----------------
def show_choice():
    """Displays which radiobutton is selected."""
    choice = selected_language.get()
    result_label.config(text=f"Selected: {choice}")


# ---------------- RADIOBUTTONS ----------------
# Radiobutton(root, text="Label", variable=shared_variable, value="value_to_store")

rb1 = tk.Radiobutton(root, text="Python", variable=selected_language, value="Python")
rb2 = tk.Radiobutton(root, text="Java", variable=selected_language, value="Java")
rb3 = tk.Radiobutton(root, text="C++", variable=selected_language, value="C++")

# Packing with spacing
rb1.pack(pady=5)
rb2.pack(pady=5)
rb3.pack(pady=5)


# ---------------- BUTTON ----------------
btn = tk.Button(root, text="Show Selection", command=show_choice)
btn.pack(pady=10)


# ---------------- LABEL FOR OUTPUT ----------------
result_label = tk.Label(root, text="Selected: ")
result_label.pack(pady=10)


# ---------------- RUN LOOP ----------------
root.mainloop()
