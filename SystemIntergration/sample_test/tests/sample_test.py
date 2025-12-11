from pytest import mark
from sample import question1, question2, question3


@mark.parametrize("input, expected", [(0, 0), (-1, -6.283), (1, 6.283)])
def test_question1(input, expected):
    '''
    Calculate the circumference of a circle given its radius r
    Params: r radius
    Return: circumference to 3 places decimal
    '''
    assert question1(input) == expected


@mark.parametrize("a, b, expected", [(0, 0, 0), (-1, -10, -1), (10, -10, 10), (1, 10, 10)])
def test_question2(a, b, expected):
    '''
    returns the maxium number from a and b
    Params: variables a and b
    Return: the largest one
    '''
    assert question2(a, b) == expected


@mark.parametrize("principal, rate, years, expected", [])
def test_question3(principal, rate, years, expected):
    '''
    Params:
        Principal (float): initial amount
        rate (float): annual interest rate as a decimal e.g. 0.05 for 5%
        years (int) Number fo years for which interest is compounded

    Returns
        float: Total amount after interest to two decimal places
    '''
    assert question3(principal, rate, years) == expected
