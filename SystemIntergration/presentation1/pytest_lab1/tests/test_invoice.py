from pytest import fixture
from pytest import mark
from invoice import load_stock, get_item_name


def test_load_stock():
    test_data = [
        ["pencil", 0.15],
        ["printer paper", 1.50],
        ["ruler", 0.55],
        ["eraser", 0.60],
        ["pen", 0.80],
        ["notebook", 1.00],
        ["folder", 1.40]
    ]

    assert load_stock("stock.txt") == test_data


@fixture
def stock_data():
    return load_stock("stock.txt")


@mark.parametrize("input, expected", [
    [0, "pencil"],
    [1, "printer paper"],
    [4, "pen"],
    [6, "folder"],
])
def test_get_item_name(input, expected, stock_data):
    assert get_item_name(stock_data, input) == expected





