"""
Test cases for 005 — Longest Palindromic Substring.

Multiple correct answers of the same length are accepted (e.g. "bab" and "aba" are both
valid for "babad"), so each test checks three properties instead of a fixed string:
  1. The result is a substring of the original input.
  2. The result is itself a palindrome.
  3. The result has the expected maximum length.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import longest_palindrome


def is_palindrome(t: str) -> bool:
    """
    Check whether t reads the same forwards and backwards.

    Args:
        t (str): String to check.

    Returns:
        bool: True if t is a palindrome.
    """
    return t == t[::-1]


def validate(s: str, result: str, expected_length: int) -> None:
    """
    Assert that result is a valid longest palindromic substring of s.

    Args:
        s (str): The original input string.
        result (str): The string returned by the solution.
        expected_length (int): The required length of the answer.
    """
    assert result in s, f"'{result}' is not a substring of '{s}'"
    assert is_palindrome(result), f"'{result}' is not a palindrome"
    assert len(result) == expected_length, (
        f"Expected length {expected_length}, got {len(result)} ('{result}')"
    )


def test_odd_length_tie():
    """Multiple valid answers exist; accept any of the same length."""
    validate("babad", longest_palindrome("babad"), 3)


def test_even_length():
    """Even-length palindrome: 'bb'."""
    validate("cbbd", longest_palindrome("cbbd"), 2)


def test_whole_string():
    """The entire string is a palindrome."""
    validate("racecar", longest_palindrome("racecar"), 7)


def test_single_character():
    """Single character is always a palindrome of length 1."""
    validate("a", longest_palindrome("a"), 1)


def test_all_same():
    """All identical characters — whole string is the answer."""
    validate("aaaa", longest_palindrome("aaaa"), 4)


def test_no_repeat():
    """No repeating characters — any single character is valid."""
    validate("abcde", longest_palindrome("abcde"), 1)


def test_palindrome_in_middle():
    """Palindrome is embedded in a longer non-palindromic string."""
    validate("xyzabacba", longest_palindrome("xyzabacba"), 7)


def test_two_chars_same():
    """Two identical characters."""
    validate("aa", longest_palindrome("aa"), 2)


def test_two_chars_different():
    """Two different characters — length 1."""
    validate("ab", longest_palindrome("ab"), 1)


def test_long_even_palindrome():
    """Even-length palindrome buried in the string."""
    validate("aacabdkacaa", longest_palindrome("aacabdkacaa"), 4)
