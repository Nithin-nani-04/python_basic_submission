import tkinter as tk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x300")


# ---------------- FUNCTION TO SHOW SELECTED ITEM ----------------
def show_selection():
    """
    Gets the index selected in the Listbox.
    Then retrieves the corresponding text.
    """
    try:
        index = listbox.curselection()[0]  # get selected index (tuple)
        item = listbox.get(index)          # get the actual text
        result_label.config(text=f"Selected: {item}")
    except IndexError:
        result_label.config(text="No item selected")


# ---------------- LISTBOX ----------------
# Listbox(root, selectmode=SINGLE or MULTIPLE)
listbox = tk.Listbox(root, width=20, height=8)
listbox.pack(pady=10)

# Add items to Listbox
languages = ["Python", "Java", "C++", "JavaScript", "Swift", "Go", "Rust"]

for lang in languages:
    listbox.insert(tk.END, lang)

# ---------------- BUTTON ----------------
btn = tk.Button(root, text="Show Selection", command=show_selection)
btn.pack(pady=10)

# ---------------- LABEL ----------------
result_label = tk.Label(root, text="Selected:")
result_label.pack(pady=10)


# ---------------- RUN APP ----------------
root.mainloop()
