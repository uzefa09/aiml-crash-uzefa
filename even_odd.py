# Task 3: Even or Odd Checker

try:
    number = int(input("Enter a number: "))
    if number == 0:
        print("That's zero!")
    elif number % 2 == 0:
        print(f"{number} is Even.")
    else:
        print(f"{number} is Odd.")
except ValueError:
    print("Not a number! Enter digits only.")