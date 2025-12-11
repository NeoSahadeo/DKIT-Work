def add(x, y):
    """
    Add x to y
    """
    return x + y


def subtract(x, y):
    """
    Subtract y from x
    """
    return x - y


def multiply(x, y):
    """
    Multiplies x by y
    """
    return x * y


def division(x, y):
    if y == 0:
        return -1
    return round(x / y, 2)
