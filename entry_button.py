from tkinter import *

root = Tk()
root.title("button")
root.geometry("600x400")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    e.delete(0, "end")

e = Entry(root, width=50)
e.pack()


byButton = Button(root, text="Enter your name", command=myClick)
byButton.pack()

root.mainloop()