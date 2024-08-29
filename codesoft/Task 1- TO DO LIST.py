import os

# Initialize an empty to-do list
todo_list = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")

def view_todo_list():
    if not todo_list:
        print("\nYour To-Do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list):
            status = "✓" if task['complete'] else "✗"
            print(f"{i+1}. {task['task']} [{status}]")

def add_task():
    task = input("\nEnter the task you want to add: ")
    todo_list.append({'task': task, 'complete': False})
    print(f"Task '{task}' added successfully.")

def edit_task():
    view_todo_list()
    if todo_list:
        task_number = int(input("\nEnter the task number you want to edit: ")) - 1
        if 0 <= task_number < len(todo_list):
            new_task = input("Enter the new task: ")
            todo_list[task_number]['task'] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

def delete_task():
    view_todo_list()
    if todo_list:
        task_number = int(input("\nEnter the task number you want to delete: ")) - 1
        if 0 <= task_number < len(todo_list):
            removed_task = todo_list.pop(task_number)
            print(f"Task '{removed_task['task']}' deleted successfully.")
        else:
            print("Invalid task number.")

def mark_task_complete():
    view_todo_list()
    if todo_list:
        task_number = int(input("\nEnter the task number you want to mark as complete: ")) - 1
        if 0 <= task_number < len(todo_list):
            todo_list[task_number]['complete'] = True
            print(f"Task '{todo_list[task_number]['task']}' marked as complete.")
        else:
            print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task_complete()
        elif choice == '6':
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
