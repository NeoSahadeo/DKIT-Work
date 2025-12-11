def read_students(file_name):
    """
    Prints out the students names' in
    the file.

    :param str file_name:
    """

    with open(file_name, "r") as file:
        for x in file:
            print(x.strip())
