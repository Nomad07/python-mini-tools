def meters_to_kilometers(meters):
    return meters / 1000


def kilometers_to_meters(kilometers):
    return kilometers * 1000


print("Choose conversion:")
print("1 - Meters to Kilometers")
print("2 - Kilometers to Meters")

choice = input("Your choice: ")

if choice == "1":
    meters = float(input("Enter meters: "))
    print("Kilometers:", meters_to_kilometers(meters))
elif choice == "2":
    kilometers = float(input("Enter kilometers: "))
    print("Meters:", kilometers_to_meters(kilometers))
else:
    print("Invalid choice")
