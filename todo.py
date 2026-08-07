tasks = []

while True:
    print("\nTodo List")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Quit")

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
            for task in tasks:
                print("-", task)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
