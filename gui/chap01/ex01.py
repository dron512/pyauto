import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("타이틀")

label = ttk.Label(win, text="A label")
label.grid(column=0,row=0)

def click_me():
    btn.configure(text=tx_name.get()+"btn_click")
    label.configure(text="btn_click")
    label.configure(foreground="red")

btn = ttk.Button(win,text="Button",command=click_me)
btn.grid(column=1,row=0)

tx_name = tk.StringVar()
name_entered = ttk.Entry(win,width=12,textvariable=tx_name)
name_entered.grid(column=0,row=1)


win.mainloop()