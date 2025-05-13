import tkinter as tk
from tkinter import ttk
import os

FILENAME = "To-Do-List Version 0.5.txt"
tasks = []  # list of (StringVar, BooleanVar)

def save_tasks():
    with open(FILENAME, "w") as file:
        for text_var, done_var in tasks:
            mark = "[x]" if done_var.get() else "[ ]"
            file.write(f"{mark} {text_var.get()}\n")

def load_tasks():
    if not os.path.exists(FILENAME):
        return
    with open(FILENAME, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("[x]"):
                add_task(line[4:], done=True)
            elif line.startswith("[ ]"):
                add_task(line[4:], done=False)

def add_task(text, done=False):
    text_var = tk.StringVar(value=text)
    done_var = tk.BooleanVar(value=done)
    checkbox = tk.Checkbutton(task_frame_inner, text=text, variable=done_var,
                              onvalue=True, offvalue=False, anchor="w",
                              command=save_tasks, wraplength=300)
    checkbox.pack(fill='x', pady=2, padx=5, anchor='w')
    tasks.append((text_var, done_var))

def add_task_from_entry(event=None):
    task_text = entry.get().strip()
    if task_text:
        add_task(task_text)
        entry.delete(0, tk.END)
        save_tasks()

# Setup main window
root = tk.Tk()
root.title("Nicolaj's To-Do List v0.5 (Tkinter Only)")
root.geometry("400x500")

# Entry box
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.bind("<Return>", add_task_from_entry)

add_btn = tk.Button(root, text="Add Task", command=add_task_from_entry)
add_btn.pack()

# Scrollable frame
canvas = tk.Canvas(root, borderwidth=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
task_frame = tk.Frame(canvas)

task_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=task_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
scrollbar.pack(side="right", fill="y")

# Inner frame to hold checkboxes
task_frame_inner = tk.Frame(task_frame)
task_frame_inner.pack(anchor="nw", fill="both", expand=True)

# Load tasks on startup
load_tasks()

root.mainloop()
