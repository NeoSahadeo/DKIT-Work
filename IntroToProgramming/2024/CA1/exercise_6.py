# Neo Sahadeo 16/10/2024

# Get the users favourite avenger.
# Call .lower() method to clean input.
favourite_avenger = input("What's your favourite Avenger: ").lower()

# A match-case for the users
# favourite avenger.
match favourite_avenger:
    case "iron man" | "tony stark" | "stark":  # check for iron man or tony stark or stark
        print("'I am Iron Man' :''') ")
    case "captain america":  # check for captain america
        print("*Ba donk* Captain America is cool!")
    case "hulk":  # check for hulk
        print("'Hulk Smash' the strongest avenger!")
    case "thor":  # check for thor
        print("*Mjölnir swirling sounds* the strongest avenger!")
    case "hawkeye":  # check for hawkeye
        print("*Arrow sounds* he should buy a gun!")
    case _:
        print(f"I'll have to look into {favourite_avenger}, I can't believe I haven't heard of them!")
