import random

for x in range(10):
    new_random = random.randint(1, 10)
    value = int(input("Enter a number [1, 10]: "))
    if new_random == value:
        print("Random value found!")
        break
    else:
        print(f"Random guess wrong {x}")
        print(f"Guesses left: {10-x}")
