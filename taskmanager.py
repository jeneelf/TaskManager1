tasks = []
count = 0


def add_task(task):
    global count
    tasks.append(task)
    count += 1
    print("Task added:", task)


def remove_task(task_index):
    global count
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        count -= 1
        print("YAY!! You've completed:", removed_task)
        print("You have", count, "tasks left.")
    else:
        print("Invalid task index")


def list_tasks():
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks in the list.")


def main():
    while True:
        print("\nMy Task List")
        print("1. Add New Task")
        print("2. Remove Task")
        print("3. List All Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
            task_index = int(input("Enter the task index to remove: ")) - 1
            remove_task(task_index)
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
