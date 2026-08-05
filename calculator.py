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

print("Addition:", add(first, second))
print("Subtraction:", subtract(first, second))
print("Multiplication:", multiply(first, second))
print("Division:", divide(first, second))
