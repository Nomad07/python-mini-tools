tasks = []

while True:
    print("\nTodo List")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Delete task")
    print("4 - Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "2":
        print("\nYour tasks:")

        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(number, "-", task)

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(number, "-", task)

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Deleted:", removed)
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
