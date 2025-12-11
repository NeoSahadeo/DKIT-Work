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
