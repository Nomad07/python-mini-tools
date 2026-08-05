first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

addition = first + second
subtraction = first - second
multiplication = first * second

if second != 0:
    division = first / second
else:
    division = "Cannot divide by zero"

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
