# Where are the grades coming from?
#   Answer: User input
# How do you take in a grades from that source?
#   Answer: input("Enter grades: ")
# How do you split up grades?
#   Answer: call the .split() method on the string
# How are you going to store it?
#   Answer: Store it in a list variable

# What does the function do?
#   Answer: Check which value in the list is the largest
# How are you going to do this?
#   Answer: Loop through all of the elements in the list comparing
#           values to the currently stored highest value?
# What type of loop?
#   Answer: A for loop
# What is the current highest value variable?
#   Answer: This is the value where the highest number in the list is stored
# How are you comparing the variables?
#   Answer: I will use the less than binary operater
# How will you pass the list to the function?
#   Answer: Passed as a parameter
# How will you display the highest grade to the user?
#   Answer: A print statement


# Pseudo code
# part 1:
# ^^^^^^^
# create a function that takes in a parameter
# create a variable in the function that stores the highest grade
# set this value to negative 1
# loop through the grades
# if there grade value is greater than the one stored I replace it
# finally I return the value or print the value

# part 2:
# ^^^^^^^
# take in user input as a single line
# split these into seperate "words"
# add these "words" to a list variable
# pass the variable into the function and call the function

def highest_grade(grades):
    highest_grade = -1
    for x in grades:
        if highest_grade < int(x):
            highest_grade = int(x)

    print(highest_grade)


grades = input("Enter grades: ").split()
highest_grade(grades)
