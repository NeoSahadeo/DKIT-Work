import random

names = ["Neo", "Shane", "Kenneth", "Kingsley", "Amanda"]

random_action = random.randint(1, 3)

print(names)

match random_action:
    case 1:
        names.append(input("Enter a name to add: "))
        print(names)
    case 2:
        user_in = input("Enter a name to remove: ").strip()
        if names.__contains__(user_in):
            names.remove(user_in)
            print(names)
    case 3:
        user_in = input("Clear the contents of the list? (y/n)").strip().lower()
        if user_in == 'y':
            names.clear()
            print(names)
