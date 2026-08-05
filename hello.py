def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")


def main():
    name = input("What is your name? ")
    greet(name)


if __name__ == "__main__":
    main()
