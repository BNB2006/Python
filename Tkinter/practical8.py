import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Practical 8")
root.geometry("300x200")

def show_info():
    messagebox.showwarning("Danger", "I told you dont click!")


btn = tk.Button(root, text="Dont click", command=show_info)
btn.pack(padx=10, pady=70)

root.mainloop()