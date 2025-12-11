import random

upper = int(input("Upperbound: "))
lower = int(input("Lowerbound: "))
gen_num = int(input("Random numbs to gen: "))

random_arr = []

for x in range(0, gen_num):
    random_arr.append(random.randint(lower, upper))


print(f"""
Random Numbers: {random_arr}
""")
