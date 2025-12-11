import random


def dice_roll():
    QUIT = False
    while not QUIT:
        user_input = input("Roll dice? (y/n): ").strip().lower()

        if user_input == 'y':
            random_number = random.randint(1, 6)
            print(random_number)

        if user_input == 'n':
            break
