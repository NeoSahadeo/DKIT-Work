option = None
username = input("Username: ")
password = input("Password: ")

if not username and not password:
    print("Log in failed")
elif username == "root" and password == "password":
    option = int(input("""
1. See some fun facts about the days of the week
2. Calculate the price of some train tickets
3. See how many days are in a month

Option (1/2/3): """))

if option:
    match option:
        case 1:
            day = input("Please enter a day of the week: ").lower()

            match day:
                case "monday":
                    print("In 2012 and 2018, there were 53 Mondays in the year.")
                case "tuesday":
                    print("The planet Uranus was discovered on a Tuesday")
                case "wednesday":
                    print("In the Adams family comic strip the daughter is called Wednesday.")
                case "thursday":
                    print("In 'The Hitchhikers Guide to the Galaxy' Auther Dent mentioned he could never get the hang of things on a Thursday.")
                case "friday":
                    print("Friday by Rebecca Black")
                case "saturday":
                    print("In astrology, Saturday is aligned to the planet Saturn.")
                case "sunday":
                    print("Sunday is named after and dedicated to the Sun.")
                case _:
                    print("That is not a valid day")
        case 2:
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
        case 3:
            month = input("Please enter a month: ").lower()

            match month:
                case "january":
                    print("31")
                case "february":
                    print("28 / 29, is it a leap year?")
                case "march":
                    print("31")
                case "april":
                    print("30")
                case "may":
                    print("31")
                case "june":
                    print("31")
                case "july":
                    print("31")
                case "august":
                    print("31")
                case "september":
                    print("30")
                case "october":
                    print("31")
                case "november":
                    print("30")
                case "december":
                    print("31")

                case _:
                    print("Not a valid month")
        case _:
            print("An error occured: Option does not exist")
