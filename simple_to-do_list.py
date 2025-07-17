todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")

def add_task():
    task = input("Enter your task: ")
    todo_list.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("Enter the task number to remove: "))
            removed = todo_list.pop(task_num - 1)
            print(f"Task '{removed}' removed.")
        except (ValueError, IndexError):
            print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option.")