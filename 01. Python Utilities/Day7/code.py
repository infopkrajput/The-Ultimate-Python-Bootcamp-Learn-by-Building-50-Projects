"""
Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os

TASK_FILE = "tasks.txt"


def load_tasks():
    tasks = []

    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.rsplit("||", 1)
                if len(parts) != 2:
                    continue

                text, status = parts
                if status not in {"done", "not_done"}:
                    continue

                tasks.append({"text": text, "status": status == "done"})
    else:
        print("No tasks found. Starting with an empty task list.")

    return tasks


def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            status = "done" if task["status"] else "not_done"
            file.write(f"{task['text']}||{status}\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["status"] else "✘"
        print(f"{index}. {task['text']} {status}")
    print()


def add_task(tasks):
    task_text = input("Enter the task description: ").strip()
    if not task_text:
        print("Task cannot be empty. Please try again.")
        return

    tasks.append({"text": task_text, "status": False})
    save_tasks(tasks)
    print("Task added successfully.")


def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            del tasks[task_number - 1]
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid number.")


def delete_completed_tasks(tasks):
    tasks[:] = [task for task in tasks if not task["status"]]
    save_tasks(tasks)
    print("All completed tasks have been deleted.")


def main():
    tasks = load_tasks()

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Delete all completed tasks")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            delete_completed_tasks(tasks)
        elif choice == "6":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
