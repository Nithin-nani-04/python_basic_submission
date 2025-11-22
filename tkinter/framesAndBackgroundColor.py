'''frame are fexible for ediiting components in tk'''
import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("my application")

my_frame=ttk.Frame()
my_frame.pack(side='left',fill='both',expand=True)



label1=tk.Label(my_frame,text="Hello world",bg="red")
label1.pack(side='left' ,fill='x',expand=True)
'''expand label used to expand the component and fill is used to utilize the all space
fill=x,y,both any one option can be valid

'''

label2=tk.Label(text="Hello world", bg="blue")
label2.pack(side='left',fill='both',expand='both')
label3=tk.Label(text="Hello world",bg="green")
label3.pack(side='left',fill='y', expand=True)


window.mainloop()