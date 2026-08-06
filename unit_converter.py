print("Choose conversion:")
print("1 - Meters to Kilometers")
print("2 - Kilometers to Meters")

choice = input("Your choice: ")

if choice == "1":
    meters = float(input("Enter meters: "))
    print("Kilometers:", meters / 1000)
elif choice == "2":
    kilometers = float(input("Enter kilometers: "))
    print("Meters:", kilometers * 1000)
else:
    print("Invalid choice")
