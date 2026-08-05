import random

number = random.randint(1, 10)
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts}. Guess the number (1-10): "))

    if guess == number:
        print(f"Correct! You guessed the number in {attempt} attempt(s).")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"You lost! The number was {number}.")
