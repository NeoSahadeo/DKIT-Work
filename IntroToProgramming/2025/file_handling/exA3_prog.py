from exA3 import find_matches

# Read in the file name and ask the user for the
# name of the file
with open(input("File name: "), "r") as file:
    data = []  # create a list for all the data

    # Iterate through each line the file
    # and append the stripped version of the
    # data to the data list
    for x in file:
        data.append(x.strip())

# Ask the user what they want to search for
search = input("Search for: ").strip()

# Look for matches in the
# this will return a list which
# can be iterated using a for-loop
for x in find_matches(data, search):
    print(x)
