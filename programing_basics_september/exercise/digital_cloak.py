# importing whole module
from tkinter import *
from tkinter.ttk import *

# importing strftime function to
# retrieve system's time
from time import strftime

# creating tkinter window
root = Tk()
root.title('Clock')

# This function is used to
# display time on the label

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

lbl = Label(root, font=('calibre', 40, 'bold'),
background='grey',
foreground='white')

lbl.pack(anchor='center')
time()

mainloop()
