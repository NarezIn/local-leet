"""
Test cases for 004 — Longest Substring Without Repeating Characters.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import length_of_longest_substring


@pytest.mark.parametrize("s, expected", [
    ("abcabcbb",  3),  # "abc"
    ("bbbbb",     1),  # "b"
    ("pwwkew",    3),  # "wke"
    ("",          0),  # empty string
    ("a",         1),  # single character
    ("au",        2),  # two unique characters
    ("aab",       2),  # duplicate at start
    ("dvdf",      3),  # "vdf"
    ("abcdef",    6),  # all unique — whole string
    ("abba",      2),  # "ab" or "ba"
    (" ",         1),  # space is a valid character
    ("a b",       3),  # includes space
    ("tmmzuxt",   5),  # "mzuxt"
    ("aaaaaa",    1),  # all same character
    ("abcdeafg",  7),  # "bcdeafg"
])
def test_length_of_longest_substring(s: str, expected: int):
    """
    Parametrized test covering standard cases, edge cases, and tricky inputs.

    Args:
        s (str): Input string.
        expected (int): Expected length of longest unique-character substring.
    """
    assert length_of_longest_substring(s) == expected
