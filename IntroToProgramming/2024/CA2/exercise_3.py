# Exercise 3 - Neo Sahadeo 07.11.2024
import random

# Manage global states
RUN_PROGRAM = True

while (RUN_PROGRAM):
    # Take in the user option
    opt = input("\nMain Menu (enter a number):\n1. Number guessing game\n2. Taxes Calculator\nTo quit type 'quit'\n")

    # Check if the user wants to quit
    if (opt == "quit"):
        break  # jump out of loop if 'quit' is entered

    # Conver the option to an integer
    # before moving on
    opt = int(opt)

    if (opt == 1):
        # Feature 1 - Number guessing game
        AMOUNT_OF_GUESSES = 5
        GAME_WON = False
        # Generate a random number in the range
        # [1,10].
        random_number = random.randint(1, 10)
        for x in range(0, AMOUNT_OF_GUESSES):
            # Take in the user guess
            guess = int(input("Enter a guess: "))

            # Check if the guess is correct
            if (guess == random_number):
                GAME_WON = True  # update the game state
                break  # jump out of the loop

        if GAME_WON:
            print("Congrats! You guessed the number!")
        else:
            print(f"WOMP WOMP! You ran out of guesses! The number was: {random_number}")

    if (opt == 2):
        # Feature 2 - Taxes :''(
        # Correct data:
        # salary - (0, inf)
        # tax_rate - (0, 100)

        # Take in the user's salary and tax rate.
        salary = float(input("Enter you salary: "))
        tax_rate = float(input("Enter your tax rate %: "))

        # Guarding if statement to check if the data is correct.
        if (salary < 0 or tax_rate < 0 or tax_rate > 100):
            print("Data entered was malformed.")
        else:
            yearly_salary_total = salary * 12  # 12 months in a year.
            tax_owed = (tax_rate / 100) * yearly_salary_total  # Make sure to normalise the tax rate.
            net_pay = yearly_salary_total - tax_owed  # Net pay is the diff
            print(f"Net Pay:  € {net_pay:0.2f}\nTax Owed: € {tax_owed:0.2f}")

    # Display a retuning to main menu when the loop
    # restarts
    print("\nReturning to main menu...\n")
