from tdd_ex2 import is_prime


def test_is_prime():
    assert is_prime(-1)
    assert is_prime(2)
    assert is_prime(17)
    assert is_prime(2843)
    assert not is_prime(16)
    assert not is_prime(15)
