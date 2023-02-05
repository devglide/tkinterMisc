from tkinter import *

root = Tk()
root.title("Button Click")
root.geometry('320x300')


def myClick():
    myLabel = Label(root, text=e.get(), fg='black', bg='white')
    myLabel.pack()

e = Entry(root, fg='black', bg='white')
e.pack()

my_button = Button(root, fg='black', bg='white',text="Submit", command=myClick)
my_button.pack()


root.mainloop()()