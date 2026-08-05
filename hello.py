def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")


name = input("What is your name? ")
greet(name)
