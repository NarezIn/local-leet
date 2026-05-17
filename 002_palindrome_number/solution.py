"""
Solution template for 002 — Palindrome Number.

Fill in the function body below, then run:
    pytest test_solution.py -v
"""


def is_palindrome(x: int) -> bool:
    """
    Determine whether an integer reads the same forwards and backwards.

    Args:
        x (int): The integer to check.

    Returns:
        bool: True if x is a palindrome, False otherwise.
    """
    s, f = 0, len(str(x)) - 1
    word = str(x)
    while s < f:
        if word[s] == word[f]:
            s += 1
            f -= 1
        else:
            return False
    return True
