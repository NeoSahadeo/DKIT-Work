def find_matches(data, value):
    """
    Find matches will return all occurences
    of a match in a list of matches
    """

    # A list used to store all of the
    # matches
    matches = []

    # Iterate over the list
    for x in data:

        # If the value is the same as the element
        # then add the element to the match list
        if x == value:
            matches.append(x)

    # Return the values
    return matches
