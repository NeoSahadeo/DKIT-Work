GROWTH_PERCENT = 0.03

current_population = 3_900_000
amount_of_years = 0

while current_population <= 10_000_000:
    current_population += current_population * GROWTH_PERCENT
    amount_of_years += 1

print(amount_of_years)
