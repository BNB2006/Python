import tkinter as tk

def update():
    global running, counter
    if running:
        counter += 1
        time_label.config(text=f"{counter}")
        root.after(1000, update)

def start():
    global running, counter
    time_label.config(text="starting")
    start_btn.config(state="disabled")
    stop_btn.config(state="normal")
    reset_btn.config(state="normal")
    root.after(500, lambda: [set_running(True), update()])

def stop():
    global running
    set_running(False)
    start_btn.config(state="normal")
    stop_btn.config(state="disabled")
    reset_btn.config(state="normal")

def reset():
    global counter
    counter = 0
    time_label.config(text="0.0")
    reset_btn.config(state="disabled")

def set_running(val):
    global running
    running = val

root = tk.Tk()
root.title("Stopwatch")
root.configure(bg='#000206')
root.geometry('200x150')

counter = 0
running = False

time_label = tk.Label(root, text="⏱️", font=("Arial", 40),fg="#0a6167", bg='#000206')
time_label.pack(pady=20)

start_btn = tk.Button(root, text="Start", command=start, font=("Arial", 12), bg="#51d342")
start_btn.pack(side="left", padx=10)

stop_btn = tk.Button(root, text="Stop", command=stop, font=("Arial", 12), bg="#e63838", state="disabled",)
stop_btn.pack(side="left", padx=10)

reset_btn = tk.Button(root, text="Reset", command=reset,font=("Arial", 12), bg="#e0dd3c", state="disabled",)
reset_btn.pack(side="left", padx=10)

root.mainloop()