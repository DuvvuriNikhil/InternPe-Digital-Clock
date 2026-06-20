import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=("Arial", 50), background="black", foreground="cyan")
label.pack(anchor="center")

def update_time():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

update_time()
root.mainloop()
