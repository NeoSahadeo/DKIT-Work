# Create text file link with read permissions
file = open("sample_numbers_3", "r")

total = 0  # Total stores the values of the ints in the file

line = file.readline()  # Read the current line into python

while line:  # continue if null terminator is not reached

    total += int(line)  # Convert the line to an int and add the value to total

    line = file.readline()  # Load the next line into python
    # replace the previous line
    # which means the file is being read
    # line-by-line


print(f"Total: {total}")  # Print out the total

file.close()  # Close the link to the file
