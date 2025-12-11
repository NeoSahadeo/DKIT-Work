# name: str = input("Please enter your name: ")
# print(f"Thanks You {name}")
#
# lucky_number: int = int(input("Please enter your lucky number: "))
#
# doubled: int = lucky_number + lucky_number
#
# print(f"Double your lucky number is {doubled}")


# A

# Exercise 1
# name: str = input("Please enter you name: ")
#
# print(f"Welcome {name} to the 'Introduction to Programming Course'")

# Exercise 2
# favourite_band: str = input("Please enter your favourite band: ")
# random_city: str = input("Please enter a random city: ")
# random_year: str = input("Please enter a random year: ")

# print(f"You saw {favourite_band} in {random_city} back in random_year")

# Exercise 3
# firstname: str = input("Please enter your firstname: ")
# lastname: str = input("Please enter your lastname: ")
#
# print(f"Hello {firstname}, I didn't know your family name was {lastname}. I know a lastname back home!")

# Exercise 4
# food: str = input("Please enter a food: ")
# name: str = input("Please enter your name: ")
# adjective: str = input("Please enter an adjective: ")
# noun: str = input("Please enter a noun: ")
# verbs: str = input("Please enter 3 verbs: ").split(" ")
#
# print(f"""It was {food} day at school, and {name} was soooo {adjective} for lunch. But when
# they went outside to eat, a {noun} stole her {food}! {name} chased the {noun}
# all over school. They {verbs[0]}, {verbs[1]}, and {verbs[2]} through the campus. Then they
# tripped on their {noun} and the {noun} got away! Luckily, {name}’s friends were
# willing to share their {food} with them.""")


# B

# Ex1
# number1: int = input("Please enter an integer: ")
# number2: int = input("Please enter an integer: ")
#
# print(f"{number1 + number2}")

# Ex2
# number1: int = int(input("Please enter an integer: "))
# number2: int = int(input("Please enter an integer: "))
# number3: int = int(input("Please enter an integer: "))
# average = (sum([number1, number2, number3]) / 3)
#
# print(f"The average between the numbers are: {average}")

# Ex3

# Cash balance at the beginning of the month.
# beginning_cash = float(input("Enter your current cash balance: "))
#
# # Amount earned in a month
# earnings = float(input("Enter the amount of money you have earned during the month: "))
#
# # Amount spent in a month
# money_spent = float(input("Enter the amount of money you have spent during the month: "))
#
# # Balance Left over
# ending_balance = beginning_cash + earnings - money_spent
#
# print(f"""
# Beginning of month:             {beginning_cash}
# Money earned in the month:      {earnings}
# Money spend during the month:   {money_spent}
#
# Balane:                         {ending_balance}
# """)

# Ex4
# discount = 0.5
# retail_items_price = float(input("Price: "))
# print(f"The discounted price: {(retail_items_price - (discount * retail_items_price)):.2f}")

# Ex5

# allems = float(input("Enter the number of allems: "))  # IDK what allems are
# conversion_factor = 35.71428571  # 1 \ 0.028
#
# print(f"Zoobies: {allems * conversion_factor}")  # Zoobies woobies

# Ex6

# number_of_acres = float(input("Please enter the number of acres you have: "))
# tons_factor = 18  # The number of tons of per acre
# print(f"Tons of Corn: {number_of_acres * tons_factor}")

# Ex7

# fahrenheits = float(input("Fahrenheits: "))
# print(f"Celcius: {((5 / 9) * (fahrenheits - 32))}")

# Ex8

# hours = int(input("Enter the number of hours spent cycling: "))
# minutes = int(input("Enter the number of minutes spent cycling: "))
#
# total_seconds = hours * 3600 + minutes  # 3600 is hours to minutes
#
# print(f"Number of seconds spent cycling: {total_seconds}")


# Ex9

# Cycling burns 200 calories per hour
# Jogging burns 475 calories per hour
# Swimming burns 275 calories per hour
# A person loses 1 pound of weight for each 3500 calories burned.

# pound_per_calorie = 2.85714286e-4  # 1/3500
#
#
# time_cycling = int(input("How many hours did you spends cycling: "))
# time_jogging = int(input("How many hours did you spends jogging: "))
# time_swimming = int(input("How many hours did you spends swimming: "))
#
# pounds_burnt = (time_cycling * 200 + time_jogging * 475 + time_swimming * 275) * pound_per_calorie
#
# print(f"Amount of pounds burnt: {pounds_burnt:.4f}")
