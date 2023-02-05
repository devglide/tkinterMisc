from tkinter import *


root = Tk()
root.title('Basic binary check box')
root. geometry("400x400")

def show():
    myLabel = Label(root, fg='black', bg='white', text=var.get()).pack()


var = IntVar()

c = Checkbutton(root, text="Check me", variable=var)
c.pack()

myButton = Button(root, text="Show", fg='black', bg='white', command=show)
myButton.pack()

root.mainloop()