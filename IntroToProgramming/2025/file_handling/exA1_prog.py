from exA1 import pretty_print

with open("exA1_data", "r") as file:
    data = []
    for x in file:
        data.append(x.strip())

pretty_print(data)

