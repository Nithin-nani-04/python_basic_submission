import tkinter as tk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("300x250")


# ---------------- VARIABLES ----------------
# Checkbuttons need a Tkinter variable to store their state.
# IntVar() → stores 1 (checked) or 0 (unchecked)
python_var = tk.IntVar()
java_var = tk.IntVar()
cpp_var = tk.IntVar()


# ---------------- FUNCTIONS ----------------
def show_selection():
    """This function prints which checkbuttons are selected."""
    selected = []

    if python_var.get() == 1:
        selected.append("Python")
    if java_var.get() == 1:
        selected.append("Java")
    if cpp_var.get() == 1:
        selected.append("C++")

    result_label.config(text=f"Selected: {', '.join(selected)}")


# ---------------- CHECKBUTTONS ----------------
# Checkbutton(root, text="Label", variable=variable)
# 'text' → label shown beside the box   --------------onvalue offvalue
# 'variable' → tracks if it is checked or unchecked

python_cb = tk.Checkbutton(root, text="Python", variable=python_var)
java_cb   = tk.Checkbutton(root, text="Java", variable=java_var)
cpp_cb    = tk.Checkbutton(root, text="C++", variable=cpp_var)

# Packing (with padding for spacing)
python_cb.pack(pady=5)
java_cb.pack(pady=5)
cpp_cb.pack(pady=5)


# ---------------- BUTTON TO SHOW RESULT ----------------
btn = tk.Button(root, text="Show Selection", command=show_selection)
btn.pack(pady=10)


# ---------------- LABEL TO DISPLAY OUTPUT ----------------
result_label = tk.Label(root, text="Selected: ")
result_label.pack(pady=10)


# ---------------- RUN THE WINDOW ----------------
root.mainloop()
