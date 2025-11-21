import tkinter as tk
import tkinter.font as tf
import tkinter.ttk as ttk

window=tk.Tk()
window.title("my application")
window.minsize(width=600,height=600)
customfont=tf.Font(family='Times New Roman',size=15)

label=ttk.Label(text="hello World",font=customfont,foreground='black',background='red')
label.pack()

#changing text in label part
# label["text"]="have a nice day"

# label.config(text='how are you?')


#Buttons
'''creating a button '''
button=ttk.Button(text="click me")
button.pack()
'''command to run when button is clicked'''
counter=0
def function_command():
    global counter#to make the counter avalible globally
    print("Thanks for clicking!") #print in console
    label.config(text=f'button got clicked {counter+1}times')
    counter+=1


button1=ttk.Button(text="hello",command=function_command,)
button1.pack()
'''-------------------------------------------This is important part------------------------------------------------------------------'''
""" the user input to screen"""
#taking user input --entry class text box
user_input=ttk.Entry(width=30,) # show is used for hidding date show='*'
user_input.pack()
print(user_input.get()) # never change any thing


def function2():
    label['text']=user_input.get()

button2=ttk.Button(text='click me to enter' ,command=function2)
button2.pack()

window.mainloop()





'''---ttk is called as themed tkinter   tkinter.ttk() 
here you have foreground and background for every thing 
'''