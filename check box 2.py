from tkinter import *


root = Tk()
root.title('Basic binary check box')
root. geometry("400x400")

def show():
    myLabel = Label(root, fg='black', bg='white', text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Check me", variable=var, onvalue="on", offvalue="off")
c.deselect()
c.pack()

myButton = Button(root, text="Show", fg='black', bg='white', command=show)
myButton.pack()

root.mainloop()