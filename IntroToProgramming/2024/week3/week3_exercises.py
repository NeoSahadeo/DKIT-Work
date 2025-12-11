# Exercise 1

# take in user input
# age = int(input("Please enter your name: "))
#
# # If user is legally old enough to vote
# if age > 18:
#     print("You can vote.")

# Exercise 2

# User login
# username = input("Username: ")
# password = input("Password: ")  # use getpass
#
# # Check if username and password are correct.
# if username == "super secret username" and password == "Secret01":
#     print("Login successful")
# else:
#     print("Login failed")

# Exercise 3

# my_number = 18
# number = int(input("Enter a number between 0 and 100"))

# Exercise B2

# if number % 5 == 0 or number % 3 == 0:  # jackpot check
#     print("You hit the jackpot!!! OMG")

# if number == my_number:
#     print("You guessed my number!")
# else:
#     print("You failed!")

# Exercise B3

# number_1 = int(input("Enter a number: "))
# number_2 = int(input("Enter another number: "))
#
# # If number 1 is bigger than number 2
# if number_1 > number_2:
#     print(number_2 - number_1)
# # If number 2 is bigger than number 1
# elif:
#     print(number_1 - number_2)

# Exercise C1

# # Ask user for number such that [1, 7]
# number = int(input("Please enter a number between 1 and 7 ([1, 7])"))
#
# # Check what day it is.
# # 1 = Monday
# # ...
# # 7 = Sunday
# if number == 1:
#     print("Monday")
# elif number == 2:
#     print("Tuesday")
# elif number == 3:
#     print("Wednesday")
# elif number == 4:
#     print("Thursday")
# elif number == 5:
#     print("Friday")
# elif number == 6:
#     print("Saturday")
# elif number == 7:
#     print("Sunday")
# else:
#     print("Invalid day index")

# Exercise C2

# Prices:
# Drogheda  = 12.50
# Dundalk   = 14.99
# Dublin    = 65
# Belfast   = 25.99

print("""
      Destinations:

      Belfast
      Drogheda
      Dublin
      Dundalk
      """)
# Get the train station destination
destination = input("Please enter destination: ")
# Get the number of tickets
number_of_tickets = int(input("Please enter the number of tickets: "))

if destination == "Drogheda":
    price = number_of_tickets * 12.50
    print(f"Ticket price: {price:.2f}")

elif destination == "Dublin":
    price = number_of_tickets * 65
    print(f"Ticket price: {price:.2f}")

elif destination == "Belfast":
    price = number_of_tickets * 25.99
    print(f"Ticket price: {price:.2f}")

elif destination == "Dundalk":
    price = number_of_tickets * 14.99
    print(f"Ticket price: {price:.2f}")

# Exercise C4

# business_mark = int(input("Please enter your Business Studies mark (percentage): "))
# science_mark = int(input("Please enter your Science mark (percentage): "))
#
# # 40% is a pass
# if business_mark >= 40 and science_mark >= 40:  # passed both
#     print("You passed both")
# elif business_mark < 40 and science_mark < 40:  # failed both
#     print("You failed both")
# elif business_mark >= 40 and science_mark < 40:  # passed business
#     print("You passed business")
# elif business_mark < 40 and science_mark >= 40:  # passed science
#     print("You passed science")

# Exercise C5

# Wage = 12.70
# 40 <= Regular pay
# 40 > x > 50 = 1.5 times pay
# 50 > = 2 times pay

# WAGE = 12.70
# hours_worked = int(input("Please enter the amount of hours worked: "))
# wage = 0  # no money to start
#
# # regular pay
# if hours_worked <= 40:
#     # Regular pay
#     wage = hours_worked * WAGE
#
# # 1.5 times pay after 40 hours
# elif hours_worked > 40 and hours_worked <= 50:
#     overtime_pay = hours_worked - 40
#
#     # Regular pay + 1.5 pay
#     wage = 40 * WAGE + overtime_pay * (1.5 * WAGE)
#
# else:
#     overtime_pay = hours_worked - 50
#
#     # Regular pay + 1.5 pay + 2 pay
#     wage = 40 * WAGE + 10 * (1.5 * WAGE) + overtime_pay * (2 * WAGE)
#
# print(f"Gross wage: {wage:.2f}")

# Exercise C6

birth_month = int(input("Please enter your birth month number (eg: October = 10): "))
try_again = False

if birth_month == 1:  # January
    print("Capricorn: December 22nd – January 19th")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 2:  # Febuary
    print("Aquarius: January 20th – February 18th")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 3:  # March
    print("Pisces: February 19th – March 20th")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 4:  # April
    print("Aries: March 21st – April 19th")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 5:  # May
    print("Taurus: April 20th – May 20th")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 6:  # June
    print("Gemini: May 21st – June 20th")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 7:  # July
    print("Cancer: June 21st – July 22nd")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 8:  # August
    print("Leo: July 23rd – August 22nd")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 9:  # September
    print("Virgo: August 23rd – September 22nd")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 10:  # October
    print("Libra: September 23rd – October 22nd")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 11:  # November
    print("Scorpio: October 23rd – November 21st")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True
elif birth_month == 12:  # December
    print("Sagittarius: November 22nd – December 21st")
    correct = input("Is this your start sign(y/n): ")
    if (correct == 'n' or correct == 'N'):
        birth_month += 20
        try_again = True

# Added 20 to each value. -> Modular Arithmetic Like
if birth_month == 21 and try_again:  # January
    print("Aquarius: January 20th – February 18th")
elif birth_month == 22 and try_again:  # Febuary
    print("Pisces: February 19th – March 20th")
elif birth_month == 23 and try_again:  # March
    print("Aries: March 21st – April 19th")
elif birth_month == 24 and try_again:  # April
    print("Taurus: April 20th – May 20th")
elif birth_month == 25 and try_again:  # May
    print("Gemini: May 21st – June 20th")
elif birth_month == 26 and try_again:  # June
    print("Cancer: June 21st – July 22nd")
elif birth_month == 27 and try_again:  # July
    print("Leo: July 23rd – August 22nd")
elif birth_month == 28 and try_again:  # August
    print("Virgo: August 23rd – September 22nd")
elif birth_month == 29 and try_again:  # September
    print("Libra: September 23rd – October 22nd")
elif birth_month == 30 and try_again:  # October
    print("Scorpio: October 23rd – November 21st")
elif birth_month == 31 and try_again:  # November
    print("Sagittarius: November 22nd – December 21st")
elif birth_month == 32 and try_again:  # December
    print("Capricorn: December 22nd – January 19th")
