"""
Test cases for 010 — Coin Change.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import coin_change


@pytest.mark.parametrize("coins, amount, expected", [
    ([1, 5, 10, 25], 36,   3),   # 25 + 10 + 1
    ([2],            3,   -1),   # impossible with only even denominations
    ([1],            0,    0),   # zero amount always needs zero coins
    ([1, 2, 5],      11,   3),   # 5 + 5 + 1
    ([1],            1,    1),   # single coin covers amount exactly
    ([1],            100, 100),  # only denomination is 1 cent
    ([2],            0,    0),   # zero amount with even denomination
    ([5, 10, 25],    30,   2),   # 25 + 5
    ([3, 5],         7,   -1),   # 7 cannot be formed: 3+3=6, 3+5=8
    ([3, 5],         11,   3),   # 3 + 3 + 5
    ([1, 5, 10, 25], 0,    0),   # amount is 0
    ([2, 5, 10, 1],  27,   4),   # 10 + 10 + 5 + 2
    ([1, 5, 10, 25], 99,   9),   # 25*3 + 10*2 + 1*4
])
def test_coin_change(coins: list[int], amount: int, expected: int):
    """
    Parametrized test covering reachable amounts, impossible amounts, and edge cases.

    Args:
        coins (list[int]): Coin denominations.
        amount (int): Target amount.
        expected (int): Expected minimum coin count, or -1 if impossible.
    """
    assert coin_change(coins, amount) == expected
