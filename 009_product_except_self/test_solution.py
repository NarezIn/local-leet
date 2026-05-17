"""
Test cases for 009 — Product of Array Except Self.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import product_except_self


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4],       [24, 12, 8, 6]),
    ([-1, 1, 0, -3, 3],  [0, 0, 9, 0, 0]),
    ([1, 1],             [1, 1]),          # minimum length
    ([2, 3],             [3, 2]),
    ([0, 0],             [0, 0]),          # two zeros — all products are 0
    ([1, 0],             [0, 1]),          # one zero
    ([0, 1],             [1, 0]),          # one zero, reversed
    ([-1, -2, -3, -4],   [-24, -12, -8, -6]),  # all negative
    ([1, 2, 3, 0, 5],    [0, 0, 0, 30, 0]),    # single zero in array
    ([1, 1, 1, 1],       [1, 1, 1, 1]),
    ([2, 2, 2, 2],       [8, 8, 8, 8]),
    ([-1, 1, -1, 1],     [-1, 1, -1, 1]),
])
def test_product_except_self(nums: list[int], expected: list[int]):
    """
    Parametrized test covering positive, negative, zero, and mixed inputs.

    Args:
        nums (list[int]): Input array.
        expected (list[int]): Expected output array.
    """
    assert product_except_self(nums) == expected
