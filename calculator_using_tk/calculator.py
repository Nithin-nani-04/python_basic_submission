import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

equation = tk.StringVar()
entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=4, justify="right")
entry.pack(fill="x", ipadx=8, ipady=15, padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('3',3,0), ('2',3,1), ('1',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(frame, text=text, width=5, height=2, command=equal)
    else:
        btn = tk.Button(frame, text=text, width=5, height=2, bd=3, command=lambda t=text: press(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

tk.Button(root, text="Clear", command=clear, width=20, height=2).pack(pady=10)

root.mainloop()
