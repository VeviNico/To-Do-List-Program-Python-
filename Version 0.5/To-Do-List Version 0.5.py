import customtkinter as ctk
import os

FILENAME = "To-Do-List Version 0.5.txt"
tasks = []  # List of (text, BooleanVar, CheckBox widget)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("To-Do List v0.5")
app.geometry("450x600")

title_label = ctk.CTkLabel(app, text="🗒️ Nicolaj's To-Do List", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=10)

# Scrollable frame for tasks
task_frame = ctk.CTkScrollableFrame(app, width=400, height=400, corner_radius=10)
task_frame.pack(pady=10)

entry = ctk.CTkEntry(app, placeholder_text="Enter a new task...", width=300)
entry.pack(pady=10)

def save_tasks():
    with open(FILENAME, "w") as file:
        for text, var, _ in tasks:
            mark = "[x]" if var.get() else "[ ]"
            file.write(f"{mark} {text}\n")

def load_tasks():
    if not os.path.exists(FILENAME):
        return
    with open(FILENAME, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("[x]"):
                add_task_to_ui(line[4:], done=True)
            elif line.startswith("[ ]"):
                add_task_to_ui(line[4:], done=False)

def add_task_to_ui(task_text, done=False):
    var = ctk.BooleanVar(value=done)
    checkbox = ctk.CTkCheckBox(task_frame, text=task_text, variable=var, corner_radius=8,
                               font=ctk.CTkFont(size=14), command=save_tasks)
    checkbox.pack(anchor="w", pady=4, padx=10)
    tasks.append((task_text, var, checkbox))

def add_task():
    task_text = entry.get().strip()
    if task_text:
        add_task_to_ui(task_text)
        entry.delete(0, 'end')  # 🧼 Clears the input field
        save_tasks()

add_btn = ctk.CTkButton(app, text="Add Task", command=add_task)
add_btn.pack(pady=5)

load_tasks()  # Load saved tasks on startup

app.mainloop()
