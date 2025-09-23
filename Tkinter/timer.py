import tkinter as tk
from time import strftime

def time_update():
    time_string = strftime('%H:%M:%S %p')
    date_string = strftime('%A, %d %B')
    time_label.config(text=time_string)
    date_label.config(text=date_string)
    time_label.after(1000, time_update)


root = tk.Tk()
root.configure(bg='#000206')
root.geometry('400x200')
root.resizable(False, False)


time_label = tk.Label(root, font=('Script MT Bold', 40),fg="#1cdae8",bg='#000206')
time_label.pack(pady=(30, 10))

date_label = tk.Label(root, font=('Script MT Bold', 20),bg='#000206',fg='#1cdae8')
date_label.pack(pady=(0, 30))

time_update()

root.mainloop()