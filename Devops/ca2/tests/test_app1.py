import pytest
import app1

def test_loadStock():
    data = app1.loadStock('stock.txt')
    assert len(data) == 3
    assert data[0] == ['pencil', 0.15, 97]
    assert data[1] == ['ruler', 0.6, 120]
    assert data[2] == ['eraser', 0.65, 130]