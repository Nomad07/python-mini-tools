import random

number = random.randint(1, 10)

guess = int(input("Guess the number (1-10): "))

if guess == number:
    print("Correct!")
else:
    print("Wrong! The number was", number)
