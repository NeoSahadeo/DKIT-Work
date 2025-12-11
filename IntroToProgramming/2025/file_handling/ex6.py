# This function will take in a file
# name then produce a list of numbers
def extract_nums(file_name):
    numbers = []
    # Open the file using the with operation
    # create a file handler called 'file'
    with open(file_name, "r") as file:

        # Iterate through every line in the file
        for x in file.read():

            # Strip of the carriage return
            value = x.strip()

            # Check if value is not empty
            if value:
                numbers.append(float(value))
    return numbers
