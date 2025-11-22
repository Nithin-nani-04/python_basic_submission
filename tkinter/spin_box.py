import tkinter as tk

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Spinbox Example")
root.geometry("300x200")


# ---------------- FUNCTION TO SHOW VALUE ----------------
def show_value():
    """
    This function displays the current value
    selected in the Spinbox.
    """
    value = spin.get()  # get current Spinbox value
    result_label.config(text=f"Selected Value: {value}")


# ---------------- SPINBOX ----------------
# Spinbox(root, from=start, to=end)
spin = tk.Spinbox(root,
                  from_=1,  # starting number
                  to=10,    # ending number
                  width=10, # width of box
                  font=("Arial", 14))
spin.pack(pady=15)


# ---------------- BUTTON ----------------
btn = tk.Button(root, text="Show Value", command=show_value)
btn.pack(pady=10)


# ---------------- LABEL ----------------
result_label = tk.Label(root, text="Selected Value: ")
result_label.pack(pady=10)


# ---------------- RUN THE APP ----------------
root.mainloop()
