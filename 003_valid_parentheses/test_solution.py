"""
Test cases for 003 — Valid Parentheses.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import is_valid


@pytest.mark.parametrize("s, expected", [
    ("()",       True),   # single pair
    ("()[]{}",   True),   # three types side by side
    ("(]",       False),  # mismatched types
    ("([)]",     False),  # interleaved, wrong order
    ("{[]}",     True),   # properly nested
    ("",         True),   # edge case: empty string (vacuously valid)
    ("(",        False),  # unclosed open bracket
    (")",        False),  # closing with nothing open
    ("]",        False),  # wrong closing bracket with empty stack
    ("(((",      False),  # all opens, no closes
    (")))",      False),  # all closes, no opens
    ("()[{}]",   True),   # deeper nesting
    ("([]{})",   True),   # multiple pairs nested inside parens
    ("{[()]}",   True),   # triple nesting
    ("([{}])()", True),   # nested then sequential
    ("([]",      False),  # one bracket left unclosed
])
def test_is_valid(s: str, expected: bool):
    """
    Parametrized test covering valid strings, mismatches, and edge cases.

    Args:
        s (str): Input bracket string.
        expected (bool): Expected validity result.
    """
    assert is_valid(s) == expected
