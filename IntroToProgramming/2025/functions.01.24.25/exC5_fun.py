SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", ";", ".", ",", "?", ]


def is_upper(x: str):
    tally = 0
    for y in x:
        if y.isalpha() and y.isupper():
            tally += 1
    return tally


def is_lower(x: str):
    tally = 0
    for y in x:
        if y.isalpha() and y.islower():
            tally += 1
    return tally


def is_digit(x: str):
    tally = 0
    for y in x:
        if y.isdigit():
            tally += 1
    return tally


def is_special(x: str):
    tally = 0
    for y in x:
        if y in SPECIAL:
            tally += 1
    return tally


def validate(password: str):
    validity = 0  # should be 5 is all valid
    uppercase = is_upper(password)
    lowercase = is_lower(password)
    numbers = is_digit(password)
    specials = is_special(password)
    length = len(password)

    if length >= 8 and length <= 20:
        validity += 1
    if lowercase >= 4:
        validity += 1
    if uppercase >= 1:
        validity += 1
    if numbers >= 2:
        validity += 1
    if specials >= 1:
        validity += 1

    if validity == 5:
        return True
    else:
        return False
