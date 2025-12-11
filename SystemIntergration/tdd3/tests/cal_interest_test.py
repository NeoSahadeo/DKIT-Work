# Neo Sahadeo - 22/02/2025

# 1. Principle less than or equal to €500 receive 1 % interest
# 2. Amounts over €500 but less than €2, 000 attract an interest rate of 2%
# 3. Amounts between €2, 000 and €100, 000 attract an interest rate of 3%
# 4. Any amount greater than €100, 000 will get 5 % interest.

# Assumption that the rate is annually
from pytest import mark
from main import cal_interest


@mark.parametrize("principle, expected", [(-1, 0), (0, 0), (499, 4.99),
                                          (500, 5), (501, 5.02), (1999, 34.98),
                                          (2000, 35.0), (2001, 35.03), (99_999, 2974.97),
                                          (100_000, 2975), (1_000_001, 47975.05), (1_000_000, 47974)])
def test_calc_interest(principle, expected):
    assert cal_interest(principle) == expected
