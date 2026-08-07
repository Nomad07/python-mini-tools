tasks = []

while True:
    task = input("Enter a task (or q to quit): ")

    if task.lower() == "q":
        break

    tasks.append(task)

print("Your tasks:")

for task in tasks:
    print("-", task)
