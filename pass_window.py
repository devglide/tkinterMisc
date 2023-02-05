from tkinter import *

root = Tk()
root.title("Pass window")
root.geometry("600x400")

def submit():
    global your_text
    your_text = first_win.get()
    #first_win.delete(0, 'end')
    sec_win.config(text="This is your text " + '"' + str(your_text) + '".' +" Now try adding something different!")
    
    
    hello = "Hello " + first_win.get()    #Another way of doing it
    myLabel = Label(root, text=hello)
    myLabel.pack()

    first_win.delete(0, 'end')   #Clear the Entry field


first_win = Entry(root, text="Enter your stuff here ...")
first_win.pack()

pass_butt = Button(root, text="Submit", command=submit)
pass_butt.pack()

sec_win = Label(root, text="")
sec_win.pack()



root.mainloop()