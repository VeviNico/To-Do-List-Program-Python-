import tkinter as tk
from tkinter import messagebox

FILENAME = "To-Do-List Version 0.4.txt"
tasks = []

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                if line.startswith("[x]"):
                    tasks.append((line[4:].strip(), True))
                else:
                    tasks.append((line[4:].strip(), False))
    except FileNotFoundError:
        pass

def save_tasks():
    with open(FILENAME, "w") as file:
        for task, done in tasks:
            mark = "[x]" if done else "[ ]"
            file.write(f"{mark} {task}\n")

def add_task(event=None):  # event=None lets it work for both button and Enter key
    task = entry.get()
    if task:
        tasks.append((task, False))
        update_list()
        save_tasks()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty input", "Please enter a task.")

def mark_done(index):
    task, done = tasks[index]
    tasks[index] = (task, not done)
    update_list()
    save_tasks()

def delete_task(index):
    tasks.pop(index)
    update_list()
    save_tasks()

def update_list():
    listbox.delete(0, tk.END)
    for i, (task, done) in enumerate(tasks):
        display = f"[x] {task}" if done else f"[ ] {task}"
        listbox.insert(tk.END, display)

# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List GUI v0.4")

entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task)  # Press Enter to add task

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

def on_task_select(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        action = messagebox.askquestion("Task Options", "Mark as done/undone?\nClick 'No' to delete.")
        if action == 'yes':
            mark_done(index)
        else:
            delete_task(index)

listbox.bind("<Double-Button-1>", on_task_select)

load_tasks()
update_list()
root.mainloop()
