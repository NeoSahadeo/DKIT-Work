option = input("Please choose a menu option:\n").lower()

match option:
    case "login":
        print("Logging in...")
    case "help":
        print("Print Help message")
    case _:
        print("That's not an option bruv")
