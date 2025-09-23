import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Login Failed!")

tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=15)

root.mainloop()