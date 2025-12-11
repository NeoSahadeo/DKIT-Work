def is_prime(n):
    if n == 1 or n == 2:
        return True

    for x in [2, 3, 4, 5, 6, 7, 8, 9]:
        if not n % x:
            return False
    return True
