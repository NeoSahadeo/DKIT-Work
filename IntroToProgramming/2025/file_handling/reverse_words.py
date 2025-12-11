# Create a file link with read permissions
file = open("sample_2", "r")

# Read in all the lines using the .readlines method()
file_list = file.readlines()

file_out = []  # Create a list to store my outputs for later

# Loop through all the lines in the file_list
for x in file_list:

    # Strip the string value to remove \n
    # Then split the text using the .split function
    sentence_list = x.strip().split(" ")

    # Next loop through the split text
    for y in sentence_list:
        # Reverse the string and append it to the file out list
        file_out.append(y[::-1])  # ::-1 means start and end at the same position 0, but traverse
                                  # the list backwards

file_out.append("\n")  # Append a \n to the end because I removed it in the for loop above

file.close()  # Close the file link

file = open("sample_2", "w")  # Open the file again with write permission this time

file.write(" ".join(file_out))  # Join the list elements together using the .join method and use
                                # a space(char 32) as the value to be placed between elements

file.close()  # Close the file link

