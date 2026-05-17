"""
Test cases for 001 — Two Sum.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import two_sum


def check(nums: list[int], target: int, result: list[int]) -> bool:
    """
    Validate that result is a correct answer without assuming a fixed output order.

    Args:
        nums (list[int]): The input array.
        target (int): The target sum.
        result (list[int]): The indices returned by the solution.

    Returns:
        bool: True if the result is valid.
    """
    i, j = result
    return (
        len(result) == 2
        and i != j
        and 0 <= i < len(nums)
        and 0 <= j < len(nums)
        and nums[i] + nums[j] == target
    )


def test_example_1():
    """Basic example from the problem statement."""
    assert check([2, 7, 11, 15], 9, two_sum([2, 7, 11, 15], 9))


def test_example_2():
    """Answer is not the first two elements."""
    assert check([3, 2, 4], 6, two_sum([3, 2, 4], 6))


def test_example_3():
    """Duplicate values — same value, different indices."""
    assert check([3, 3], 6, two_sum([3, 3], 6))


def test_negative_numbers():
    """Array contains negative integers."""
    assert check([-1, -2, -3, -4, -5], -8, two_sum([-1, -2, -3, -4, -5], -8))


def test_mixed_sign():
    """Target is achieved by a negative and a positive number."""
    assert check([1, -3, 5, 7], 2, two_sum([1, -3, 5, 7], 2))


def test_large_values():
    """Values near the constraint boundary."""
    assert check([10**9, -(10**9), 1, -1], 0, two_sum([10**9, -(10**9), 1, -1], 0))


def test_answer_at_end():
    """The pair is the last two elements."""
    assert check([1, 2, 3, 4, 5], 9, two_sum([1, 2, 3, 4, 5], 9))


def test_two_element_array():
    """Minimum-length array — only one possible pair."""
    assert check([5, 6], 11, two_sum([5, 6], 11))
