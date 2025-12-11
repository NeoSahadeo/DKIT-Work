GROWTH_PERCENT = 0.1
PROJECTION = 5  # The growth project in yrs

current_population = 3_900_000

for x in range(5):
    current_population += current_population * 0.1

print(f"{current_population:.0f}")
