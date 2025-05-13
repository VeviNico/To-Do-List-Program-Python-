tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")

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
        print(f"Added: {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            try:
                num = int(input("Enter the task number to remove: "))
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            except (IndexError, ValueError):
                print("Invalid number!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 4.")
