day = input("Do you wish to continue? (oui / o / non / n): \n").lower()

match day:
    case "oui" | "o":
        print("Eggselent, continue programming")
    case "non" | "n":
        print("Termination")
