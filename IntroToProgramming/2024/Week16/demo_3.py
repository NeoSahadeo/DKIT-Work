def calc_ticket_cost(destination, quantity):
    fare = -1

    if destination == 'drogheda':
        fare = 12.50
    elif destination == 'dundalk':
        fare = 14.99
    elif destination == 'belfast':
        fare = 65
    elif destination == 'dublin':
        fare = 25.99

    return quantity * fare

destination = input("Please enter a destination: ").strip().lower()
quantity = int(input("How many tickets: "))

cost = calc_ticket_cost(destination=destination, quantity=quantity)

print(f"The cost will be: {cost}")
