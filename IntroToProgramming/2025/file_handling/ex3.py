# Create a list of the week days
weekdays = ["Mon", "Tues", "Wed", "Thurs", "Fri"]


# Create a file link with append permissions
file = open("sample_weekdays.txt", "a")


# Loop through the weekdays to then write to this file
for day in weekdays:
    file.write(f"{day}\n")  # Write the day plus a new line

# Close the file link
file.close()
