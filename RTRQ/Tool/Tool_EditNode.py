import sys
sys.path.append("./")


import tkinter as tk
from tkinter import ttk
import RTRQ.kernel as kernel


app = tk.Tk()
value = kernel.kernel.getlist_Region()
cb1 = ttk.Combobox(app, values=value)
cb2 = ttk.Combobox(app, values=[])
et1 = tk.Entry(app)
btn1 = tk.Button(app,text="Set")

cb1.pack(padx=5,pady=10)
cb2.pack(padx=5,pady=10)
et1.pack(padx=5,pady=10)
btn1.pack(padx=5,pady=10)

def on_combobox_select(event):
    list_node = cb1.get()  # Get the selected value from the first combobox
    cb2.configure(values=kernel.kernel.getlist_Node(list_node))

# Bind an event to the combobox
cb1.bind("<<ComboboxSelected>>", on_combobox_select)

def on_button_click():
    Region  = cb1.get()
    Node = cb2.get()
    data = et1.get()  # Get text from the Entry widget
    kernel.kernel.set_Node(Region,Node,data)

btn1.configure(command=on_button_click)


app.mainloop()
