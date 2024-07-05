# Simple To-Do List app

tasks = []  # List to store tasks

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def list_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

while True:
    print("\nTo-Do List App")
    print("1. Add task")
    print("2. List tasks")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        task_name = input("Enter task name: ")
        add_task(task_name)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

