# Neo Sahadeo - 11/02/2025

grades = input("Enter grades: ").split()
tally_counter = []

for x in grades:
    counter = 0
    for y in grades:
        if x == y:
            counter += 1
    tally_counter.append(counter)

highest = 0
for x in tally_counter:
    if x > highest:
        highest = x

index = 0
for x in tally_counter:
    if highest == x:
        print(f"Most: {grades[index]}")
        break
    index += 1
