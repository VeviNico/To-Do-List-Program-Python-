tasks = []
FILENAME = "To-Do-List Version 0.2.txt"

# Load task from file (if it exists)
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # File doesn't exist yet

# Save all tasks to file
def save_tasks():
    print("Saving tasks to file...")  # Debug line
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
	
load_tasks()  # Load existing tasks when program starts.

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        save_tasks()
        print(f"Added: {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            try:
                num = int(input("Enter the task number to remove: "))
                removed = tasks.pop(num - 1)
                save_tasks()
                print(f"Removed: {removed}")
            except (IndexError, ValueError):
                print("Invalid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")

input("Press Enter to exit...")  # Keeps window open if double-clicked