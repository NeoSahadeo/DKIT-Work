# Neo Sahadeo - 07/10/2025

def highest_grade(grades):
    highest_grade = -1
    for x in grades:
        if highest_grade < int(x):
            highest_grade = int(x)

    print("Highest: ", highest_grade)
    return highest_grade  # added a return for the test


# Neo Sahadeo - 10/10/2025


def avg(grades):
    total = 0
    length = 0
    for x in grades:
        total += int(x)
        length += 1

    print(f"Average: {total / length}")
    return total / length  # added a return for the test

# Neo Sahadeo - 11/02/2025


def most(grades):
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

    return grades[index]  # added for tests

# Neo Sahadeo - 11/10/2025


def lowest_grade(grades):
    lowest = 101
    for x in grades:
        if lowest > int(x):
            lowest = int(x)

    print("Lowest: ", lowest)
    return lowest  # added for tests
