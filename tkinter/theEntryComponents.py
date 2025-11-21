import tkinter as tk
import tkinter.font as tf

window=tk.Tk()
window.title("my application")
window.minsize(width=600,height=600)
customfont=tf.Font(family='Times New Roman',size=15)

label=tk.Label(text="hello World",font=customfont)
label.pack()

#changing text in label part
# label["text"]="have a nice day"

# label.config(text='how are you?')


#Buttons
'''creating a button '''
button=tk.Button(text="click me")
button.pack()
'''command to run when button is clicked'''
counter=0
def function_command():
    global counter#to make the counter avalible globally
    print("Thanks for clicking!") #print in console
    label.config(text=f'button got clicked {counter+1}times')
    counter+=1


button1=tk.Button(text="hello",command=function_command)
button1.pack()
'''-------------------------------------------This is important part------------------------------------------------------------------'''
""" the user input to screen"""
#taking user input --entry class text box
user_input=tk.Entry(width=30,) # show is used for hidding date show='*'
user_input.pack()
print(user_input.get()) # never change any thing


def function2():
    label['text']=user_input.get()

button2=tk.Button(text='click me to enter' ,command=function2)
button2.pack()

window.mainloop()