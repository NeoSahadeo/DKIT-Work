number_of_tickets = int(input("Please enter the number of tickets you would like: "))

print("""Drogheda\t12.50
Dundalk\t\t14.99
Belfast\t\t65
Dublin\t\t25.99
""")

destination = input("Where do you want to go to: ").lower()

match destination:
    case "drogheda":
        print(f"Cost: {number_of_tickets * 12.50:.2f}")
    case "dundalk":
        print(f"Cost: {number_of_tickets * 14.99:.2f}")
    case "belfast":
        print(f"Cost: {number_of_tickets * 65:.2f}")
    case "dublin":
        print(f"Cost: {number_of_tickets * 25.99:.2f}")
    case _:
        print("Unknown station")
