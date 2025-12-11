def read_data(file_name):
    """
    Read data will take in the file name and return the
    data of the file as a dictionary where
    data = { 'username': account_balance }
    """

    # Create a variable to store the parsed data
    parsed_data = {}

    # Open the file in read mode and create a TextIOWrapper object
    file = open(file_name, 'r')

    # Iterate through ever line in the file
    # Use enumerate to return both the index and the value
    for index, value in enumerate(file.readlines()):

        # Strip and split the values on commas
        value = value.strip().split(",")

        # Check if the value exists and then check if it meets the required
        # length of 2; username+account_balance = 2
        if value and len(value) == 2:
            # Assume that the values are 'username','account_balance'
            parsed_data[value[0]] = float(value[1])  # Convert the second value in value to a float

    file.close()  # Close the file handler

    return parsed_data  # Return the data


def write_data(data, file_name):
    """
    Write Data to a file.
    Data is assumed to be 'username': 'account_balance'
    """

    # Open the file in write mode and create a TextIOWrapper object
    file = open(file_name, 'w')

    # Use the dict.items() method to return a tuple of the
    # values pairs [aka items] in the list.
    # Then use tuple unpacking to assign the
    # values to username and account balance
    for username, account_balance in data.items():

        # Use a f string to write the values in a csv format
        file.write(f"{username},{account_balance}\n")  # Make sure to add a new line

    file.close()  # Close the file handler
