import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    length = int(input("Enter password length: "))
    print("Generated password:", generate_password(length))


if __name__ == "__main__":
    main()
