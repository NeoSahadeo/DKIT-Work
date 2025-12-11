import math


def question1(r):
    '''
    Calculate the circumference of a circle given its radius r
    Params: r radius
    Return: circumference to 3 places decimal
    '''

    circumference = 2 * math.pi * r
    return round(circumference, 3)


def question2(a, b):
    '''
    returns the maxium number from a and b
    Params: variables a and b
    Return: the largest one
    '''

    if a >= b:
        return a
    else:
        return b


def question3(principal, rate, years):
    '''
    Params:
        Principal (float): initial amount
        rate (float): annual interest rate as a decimal e.g. 0.05 for 5%
        years (int) Number fo years for which interest is compounded

    Returns
        float: Total amount after interest to two decimal places
    '''
    breakpoints = [1, 3, 6]  # in years
    breakpoint_rates = [0.04, 0.05, 0.07]  # interest rate

    total = principal

    for i in range(years):
        if i + 1 in breakpoints:
            rate = breakpoint_rates[breakpoints.index(i + 1)]
        total *= (1 + rate)
    return round(total, 2)
