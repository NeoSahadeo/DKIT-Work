import random

# The amount of guesses the user needed
# to guess the number
guesses = 0
random_number = random.randrange(1, 100)

while True:
    if int(input("Enter a number in the range (0, 100): ")) == random_number:
        break
