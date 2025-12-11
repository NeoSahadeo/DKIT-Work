from src.file_handling import write_data, read_data
from src.menu import print_menu, log, DEFAULT_COLORS


def pick_user():
    """
    Ask the user which account they want to use
    and return if that user if the user exists
    """
    user = None  # Initialise to none

    # Add a while loop to wait till a valid user name is entered,  .get will return a None value if the value does not exist
    while not data.get(user):
        for x in data.keys():  # Printing out the keys are the usernames
            log(x, "\033[40;36m")

        # Continously ask the user for an account until a valid account is entered
        log("Pick a user account: ", DEFAULT_COLORS)
        user = input().strip()

        # If a user is found then the loop should break
        if data.get(user) is not None:
            log(f"User: {user}", DEFAULT_COLORS)
            break
        log(f"{user}: Not a valid user", "\033[1;31;40m")

    # Return the account name
    return user


def main():
    # Have a while loop so it runs forever until it encounters and error or break
    while True:
        # Print out the main menu
        print_menu()
        # Take in the user input and strip the value
        log("Choose an option: ", DEFAULT_COLORS, False)
        user_input = input().strip()

        match user_input:
            case '1':
                # Get the user account
                user_account = pick_user()
                # Ask the user to enter the money they want to deposit
                log("How much do you want to deposit: ", DEFAULT_COLORS)
                value = float(input().strip())
                data[user_account] += value  # Add money to the account

            case '2':
                # Get the user account
                user_account = pick_user()

                # Ask the user to enter the money they want to withdraw
                log("How much do you want to withdraw: ", DEFAULT_COLORS)
                value = float(input().strip())

                # I could add logic for not allowing the values greater
                # than the account balance but this is cool
                data[user_account] -= value  # Subtract the values
                ...
            case '3':
                # Get the user account
                user_account = pick_user()

                # Print the balance
                log(f"Balance \n{user_account}: {data[user_account]}", "\033[1;31;40m")
                ...
            case '4':
                break  # break if its an exit
            case _:  # Default case
                log("Option does not exist! Try again.", "\033[31;40m")


if __name__ == "__main__":
    # Read in the data from the file
    data = read_data('database/bank.csv')

    # Run the main function
    main()

    # Print a message to say goodbye
    log("Goodbye!", "\033[31;40m")

    # Save the data back to the file
    write_data(data, 'database/bank.csv')
