import random

# Get the amount of random numbers the user wants
random_nums = int(input("How many random numbers?: "))


# Get the range of the random numbers
range_min = int(input("What should be the smallest number?: "))
range_max = int(input("What should be the heighest number?: "))

# Check if the max range is actually bigger than the smallest range
if range_min > range_max:
    temp = range_max  # Store the smaller value
    range_max = range_min  # Overwrite the smaller value with the larger one
    range_min = temp  # Put the larger value into range_max


# Create a lost for random numbers
random_numbers = []

# Do a for-loop for the random_nums
for x in range(0, random_nums):
    # Use random .randit to generate a random number between the 
    # 2 ranges
    # Then push that into the list
    random_numbers.append(str(random.randint(range_min, range_max))+"\n")


# Create a link to the file in append mode
file_handler = open("random_numbers_2", "w")

# Write line loops through the list to write the numbers
file_handler.writelines(random_numbers)

# # Loop through the random numbers
# for x in random_numbers:
#     # Make sure value is a string.
#     # and add a character return to the end of the line
#     file_handler.write(str(x)+"\n")  # Write out the value to the file

file_handler.close()  # Close the link to the file handler






