from invoice import get_item_name, item_list, load_stock, get_price
import pytest


@pytest.fixture
def testStock():
    return load_stock("stock.txt")


def test_load_stock(testStock):
    assert testStock[0][0] == "pencil"
    assert testStock[0][1] == 0.15


@pytest.mark.parametrize("input, expected", [(0, "pencil"), (1, "printed paper"), (6, "folder")])
def test_get_item_name(testStock, input, expected):
    assert get_item_name(testStock, input)


def test_get_price(testStock):
    assert get_price(testStock, 6) == 1.40


def test_item_list(testStock):
    assert len(item_list(testStock)) == 7
