import tkinter as tk
 
window_main = tk.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("400x200")
 
entry_1 = tk.StringVar()
 
entry_widget_1 = tk.Entry(window_main, textvariable=entry_1)
entry_widget_1.pack()
 
def submitValues():
    print(entry_1.get())
 
submit = tk.Button(window_main, text="Submit", command=submitValues)
submit.pack()

 

window_main.mainloop()