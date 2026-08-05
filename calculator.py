def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    return "Cannot divide by zero"


first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

print("Choose operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Your choice: ")

if choice == "1":
    print("Result:", add(first, second))
elif choice == "2":
    print("Result:", subtract(first, second))
elif choice == "3":
    print("Result:", multiply(first, second))
elif choice == "4":
    print("Result:", divide(first, second))
else:
    print("Invalid choice")
