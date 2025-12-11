import random

numbers_generated = 0
average = 0

while True:
    random_number = random.randrange(6, 10)
    average += random_number
    numbers_generated += 1

    if random_number == 6:
        break

print(f"""
Average: {average}
Numbers Generated: {numbers_generated}
      """)
