def meters_to_kilometers(meters):
    return meters / 1000


def kilometers_to_meters(kilometers):
    return kilometers * 1000


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462


def pounds_to_kilograms(pounds):
    return pounds / 2.20462


def main():
    print("Choose conversion:")
    print("1 - Meters to Kilometers")
    print("2 - Kilometers to Meters")
    print("3 - Celsius to Fahrenheit")
    print("4 - Fahrenheit to Celsius")
    print("5 - Kilograms to Pounds")
    print("6 - Pounds to Kilograms")

    choice = input("Your choice: ")

    if choice == "1":
        meters = float(input("Enter meters: "))
        print("Kilometers:", meters_to_kilometers(meters))
    elif choice == "2":
        kilometers = float(input("Enter kilometers: "))
        print("Meters:", kilometers_to_meters(kilometers))
    elif choice == "3":
        celsius = float(input("Enter Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(celsius))
    elif choice == "4":
        fahrenheit = float(input("Enter Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(fahrenheit))
    elif choice == "5":
        kilograms = float(input("Enter kilograms: "))
        print("Pounds:", kilograms_to_pounds(kilograms))
    elif choice == "6":
        pounds = float(input("Enter pounds: "))
        print("Kilograms:", pounds_to_kilograms(pounds))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
