import pytest

from pytest_pract1 import question1, question2, question3, question4


@pytest.mark.parametrize("input, expected", [(0, 2), (17, 19), ("Hello", -1)])
def test_question1(input, expected):
    assert question1(input) == expected, "NaN did not return a -1"


@pytest.mark.parametrize("x,y,z, expected", [(0, 4, 2, 4), (-4, -3, -2, -2), (0, 1, "Hello", -1)])
def test_question2(x, y, z, expected):
    assert question2(x, y, z) == expected, "One of the variables is a NaN"


@pytest.mark.parametrize("input, expected", [
    (-1, 0),
    (99, 2.97),
    (100, 3),
    (101, 5.05),
    (999, 49.95),
    (1001, 65.065),
    (1000000, 65000),
])
def test_question3(input, expected):
    assert question3(input) == expected


@pytest.fixture()
def load_file():
    file = open("results.txt", "r")
    file_data = file.readlines()
    return file_data


@pytest.mark.parametrize("input", [17, 34, 68, 8, 25, ])
def test_question4(load_file, input):
    for x in load_file:
        values = x.strip().split(", ")
        assert question4(values, values[0]) == input
