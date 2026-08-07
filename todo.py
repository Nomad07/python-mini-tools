tasks = []

while True:
    print("\nTodo List")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Delete task")
    print("4 - Complete task")
    print("5 - Save and Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append({"name": task, "completed": False})
        print("Task added.")

    elif choice == "2":
        print("\nYour tasks:")

        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                status = "✓" if task["completed"] else " "
                print(f"{number}. [{status}] {task['name']}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(number, "-", task["name"])

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Deleted:", removed["name"])
            else:
                print("Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to complete.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(number, "-", task["name"])

            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["completed"] = True
                print("Task completed.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for task in tasks:
                status = "1" if task["completed"] else "0"
                file.write(f"{status}|{task['name']}\n")

        print("Tasks saved.")
        break

    else:
        print("Invalid choice.")

    else:
        print("Invalid choice.")
    else:
        print("Invalid choice.")
