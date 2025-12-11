import math
AMOUNT = 10

number_list = []

for x in range(0, 10):
    number_list.append(int(input("Enter a number: ")))


print(f"""
First: {number_list[0]}
Last: {number_list[-1]}
Middle: {number_list[math.floor(AMOUNT / 2) - 1]}
Avg: {sum(number_list) / AMOUNT}
""")
