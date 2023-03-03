name = input("What is your name? ")

print("Hello,", name, "! Welcome to our application.")

while True:
    number = int(input("Please enter an integer between 1 and 100 inclusive, " + name + ": "))
    if number < 1 or number > 100:
        print("Invalid input. Please input a positive integer between 1 and 100")
        break
    if number % 2 == 1 and number < 60:
        print(number, "is odd and less than 60, " + name + ".")
    elif number % 2 == 0 and 2 <= number <= 24:
        print(number, "is even and less than 25, " + name + ".")
    elif number % 2 == 0 and 26 <= number <= 60:
        print(number, "is even and between 26 and 60 inclusive, " + name + ".")
    elif number % 2 == 0 and number > 60:
        print(number, "is even and greater than 60, " + name + ".")
    elif number % 2 == 1 and number > 60:
        print(number, "is odd and greater than 60, " + name + ".")

    choice = input("Do you want to continue, " + name + "? (y/n): ")

    if choice.lower() == 'n':
        break

print("Goodbye, " + name + "! Thanks for using our application.")
