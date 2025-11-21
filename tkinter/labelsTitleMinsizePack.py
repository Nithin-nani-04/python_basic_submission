import tkinter as tk

window=tk.Tk()
#title of window
window.title("Application name")
window.minsize(width=800,height=600)#using pixcel values we are resizing the window size that is minmum size
#label in the window
label= tk.Label(text="text to here",)
label.pack() # to bring label component to window pack method is used

#changing font style in label option we have lot of option

label= tk.Label(text="text to here", font=("Times New Roman",20,"bold"))
label.pack()
import tkinter.font as tfont
custom_font=tfont.Font(family='Times New Roman',size=15,slant='italic')
#font=custom_font in label

label.config(font=("Courier",25,"underline"))
#configaration of labels after declaration

#packer
label.pack(side="left")
label.pack(expand=True)# to bring text to middle





window.mainloop()