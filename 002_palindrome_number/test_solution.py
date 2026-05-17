"""
Test cases for 002 — Palindrome Number.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import is_palindrome


@pytest.mark.parametrize("x, expected", [
    (121,        True),   # standard palindrome
    (-121,       False),  # negative numbers are never palindromes
    (10,         False),  # trailing zero breaks it
    (0,          True),   # zero is a palindrome
    (1,          True),   # single digit
    (9,          True),   # single digit
    (11,         True),   # two identical digits
    (12,         False),  # two different digits
    (1221,       True),   # even-length palindrome
    (12321,      True),   # odd-length palindrome
    (123,        False),  # not a palindrome
    (1000021,    False),  # large non-palindrome
    (2147483647, False),  # max 32-bit int, not a palindrome
    (-1,         False),  # negative single digit
    (100,        False),  # ends in zero
])
def test_is_palindrome(x: int, expected: bool):
    """
    Parametrized test covering palindromes, non-palindromes, edge cases.

    Args:
        x (int): Input integer.
        expected (bool): Expected result.
    """
    assert is_palindrome(x) == expected
