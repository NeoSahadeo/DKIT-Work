# This is a list
# to store my
# tasks.
tasks = []

# Create a file link using the
# open() function.
# Uses with so that I don't have
# to manually call a close.
print("Loading Data...")  # Helpful message to tell the user what is happening
with open("tasks", "r") as file:

    # Loop through the file and
    # read in the lines to store it
    # in a list
    for x in file:
        tasks.append(x)
    file.close()  # Manually close it because I need to read from it later

print("Data Loaded Successfully!")  # Helpful message to tell the user what is happening


# Have some options stored up here.
# It should correspond for the match to
# work
option = [
    "Add task",  # 0
    "View all tasks",  # 1
    "Remove task",  # 2
    "Exit"  # 3
]


print("===============================")  # add something to seperate the program parts

# Start the program. using a while
# loop I can conditionally exit the loop
while True:

    # Menu screen
    print("Select an option and hit enter:")

    # Use the enumerate python function
    # to return both the value and index
    # position
    for index, value in enumerate(option):
        print(f"{index}) {value}")

    # ask the user for an option
    user_input = input("").strip()

    print("===============================")  # add something to seperate the program parts
    match user_input:
        case "0":
            # Include new line as well
            tasks.append(input("Enter the task: ") + "\n")  # Add a task to the task list
            with open("tasks", "w") as file:
                file.writelines(tasks)
        case "1":
            # Display all the tasks
            print("Tasks:\n------")
            for x in tasks:
                print(x, end="")
        case "2":
            # Display all the tasks
            # uses enumerate so I get the index and value
            # back at the same time.
            print("Tasks:\n------")
            for index, value in enumerate(tasks):
                print(f" {index}) {value}", end="")

            # ask the user what item they want to remove
            search = int(input("Name of item to remove: ").strip())

            # Remove the item from the list
            # then write the changes to the file
            tasks.pop(search)
            with open("tasks", "w") as file:
                file.writelines(tasks)
        case "3":
            break
        case _:
            print("Option does not exist. Try again.")

    print("===============================")  # add something to seperate the program parts
