import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")
root.title("Separator & Padding Example")


text=tk.Text(height=60,width=60)
text.pack()
text.focus()

text.insert("1.0","hello world")
text['state']='disabled'

# ------------------ LEFT TEXT ------------------
left_text = tk.Text(root, width=20, height=10)
left_text.pack(side="left", padx=20, pady=20)
left_text.config(padx=10, pady=10)
left_text.insert("end", "Left Text\nwith padding.")

# ------------------ VERTICAL SEPARATOR ------------------
sep = ttk.Separator(root, orient="vertical")
sep.pack(side="left", fill="y", padx=10)

# ------------------ RIGHT TEXT ------------------
right_text = tk.Text(root, width=20, height=10)
right_text.pack(side="left", padx=20, pady=20)
right_text.config(padx=10, pady=10)
right_text.insert("end", "Right Text\nwith padding.")

root.mainloop()
