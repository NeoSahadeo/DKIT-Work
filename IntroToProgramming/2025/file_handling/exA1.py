import math

def pretty_print(data):
    """
    Prints out the list in a pretty way!
    """
    bar = "―"
    padding = 4

    # Sort the data based on the string length 
    # lambda x: len(x) returns the length of each
    # string and uses that as the sort criteria
    # also reverse list
    # alsoalso sort based on string on int
    try:
        int(data[0])
        data.sort(key = lambda x : int(x), reverse = True)
    except:
        data.sort(key = lambda x : len(x), reverse = True)

    # This is always the largest element
    largest_len = len(data[0])

    # Calculate the width of the list box
    width = largest_len + padding + 4

    print(bar*width)  # Prints the top of the box

    # iterate over the data and print
    # out the vaule in a nice looking
    # way
    count = 0
    for x in data:
        count += 1
        spaces = width - (len(x) + 6)
        print(f"| {count}) {x}{' ' * (spaces)}|")

    print(bar*width)  # Prints the bottom of the box

