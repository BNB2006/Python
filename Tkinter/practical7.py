import tkinter as tk

root = tk.Tk()
root.geometry("300x100")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14), fg="#B54CBD", bg="#000000")
label.pack(pady=40)

root.mainloop()