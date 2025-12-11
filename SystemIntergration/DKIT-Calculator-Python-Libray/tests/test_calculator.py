import pytest
from calculator import add, subtract, multiply, division


def test_add():
    assert add(3, 5) == 8


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 5) == 15


@pytest.mark.parametrize("x, y, expected", [
    [1, 3, 0.33],
    [4, 4, 1.0],
    [1, 0, -1],
])
def test_division(x, y, expected):
    assert division(x, y) == expected
