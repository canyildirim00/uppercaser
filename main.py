from tkinter import *
import pyperclip as pc

def upper():
    x = entry.get()
    y = x.upper()
    output.config(text= f"{y}")
    #Used pyperclip in order to autocopying and saving time.
    pc.copy(y)

window = Tk()
window.title("Uppercase")
window.config(padx=20, pady=20)

label = Label(text="Write your text here.")
label.grid(column=0, row=0)

entry = Entry()
entry.grid(column=1, row=0)

button = Button(text="Make it Upper and Copy!", command=upper)
button.grid(column=0, row=1)

output = Label(text="")
output.grid(column=1, row=1)

window.mainloop()
