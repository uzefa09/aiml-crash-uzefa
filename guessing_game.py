# Task 8: Number Guessing Game

import random

secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    try:
        guess = int(input("Guess a number (1-100): "))
        attempts += 1

        if guess == secret:
            print(f"Correct! You got it in {attempts} attempts!")
            break
        elif guess < secret:
            print(f"Too low! {max_attempts - attempts} attempts left.")
        else:
            print(f"Too high! {max_attempts - attempts} attempts left.")
    except ValueError:
        print("Enter a valid number!")
else:
    print(f"Game over! The number was {secret}.")