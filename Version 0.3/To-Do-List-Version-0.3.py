FILENAME = "To-Do-List Version 0.3.txt"
tasks = []

# Load tasks from file
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

# Save tasks to file
def save_tasks():
    print("Saving tasks to file...")  # Debug line
    with open(FILENAME, "w") as file:
        for task, done in tasks:
            mark = "[x]" if done else "[ ]"
            file.write(f"{mark} {task}\n")

# Show the main menu
def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Mark task as not done")
    print("6. Quit")

load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, (task, done) in enumerate(tasks, 1):
                mark = "[x]" if done else "[ ]"
                print(f"{i}. {mark} {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append((task, False))
        save_tasks()
        print(f"Added: {task}")

    elif choice == "3":
        try:
            num = int(input("Enter task number to remove: "))
            removed = tasks.pop(num - 1)
            save_tasks()
            print(f"Removed: {removed[0]}")
        except:
            print("Invalid number!")

    elif choice == "4":
        try:
            num = int(input("Enter task number to mark as done: "))
            task, _ = tasks[num - 1]
            tasks[num - 1] = (task, True)
            save_tasks()
            print(f"Marked as done: {task}")
        except:
            print("Invalid number!")

    elif choice == "5":
        try:
            num = int(input("Enter task number to mark as NOT done: "))
            task, _ = tasks[num - 1]
            tasks[num - 1] = (task, False)
            save_tasks()
            print(f"Marked as not done: {task}")
        except:
            print("Invalid number!")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose from 1 to 6.")

input("Press Enter to exit...")
