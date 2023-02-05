import tkinter


window = tkinter.Tk()
counter = tkinter.IntVar()
counter.set(0)
def click(var, value):
    var.set(var.get() + value)
frame = tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame, text='Up', command=lambda: click(counter, 1))
button.pack()
button = tkinter.Button(frame, text='Down', command=lambda: click(counter, -1))
button.pack()
label = tkinter.Label(frame, textvariable=counter)
label.pack()
window.mainloop()