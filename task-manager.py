import json
import os

# Define the file to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from the file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            # Ensure each task has 'title' and 'completed' keys
            for task in tasks:
                if 'title' not in task:
                    task['title'] = "Untitled Task"
                if 'completed' not in task:
                    task['completed'] = False
            return tasks
    return []


# Save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, 1):
            title = task.get('title', 'No Title')
            status = "✔️" if task.get('completed', False) else "❌"
            print(f"{idx}. {title} - {status}")

# Add a new task
def add_task(tasks):
    title = input("Enter the task title: ")
    task = {"title": title, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

# Update a task's completion status
def update_task(tasks):
    list_tasks(tasks)
    idx = int(input("Enter the task number to update: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]['completed'] = not tasks[idx]['completed']
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    list_tasks(tasks)
    idx = int(input("Enter the task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        removed_task = tasks.pop(idx)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['title']}")
    else:
        print("Invalid task number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. List tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()