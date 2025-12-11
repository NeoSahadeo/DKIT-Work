from tdd_ex1 import devops


def test_devops():
    assert devops(3) == "Dev"
    assert devops(5) == "Ops"
    assert devops(15) == "DevOps"
    assert devops(2) == "2"
