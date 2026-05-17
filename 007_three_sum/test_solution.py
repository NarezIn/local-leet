"""
Test cases for 007 — 3Sum.

Triplet order within each result and order of results in the outer list both don't matter,
so each test sorts both the expected and actual results before comparing.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import three_sum


def normalize(triplets: list[list[int]]) -> list[list[int]]:
    """
    Sort each triplet and sort the list of triplets for order-independent comparison.

    Args:
        triplets (list[list[int]]): Raw triplets from the solution.

    Returns:
        list[list[int]]: Sorted triplets in a canonical form.
    """
    return sorted(sorted(t) for t in triplets)


@pytest.mark.parametrize("nums, expected", [
    (
        [-1, 0, 1, 2, -1, -4],
        [[-1, -1, 2], [-1, 0, 1]],
    ),
    (
        [0, 1, 1],
        [],
    ),
    (
        [0, 0, 0],
        [[0, 0, 0]],
    ),
    (
        [-2, 0, 1, 1, 2],
        [[-2, 0, 2], [-2, 1, 1]],
    ),
    (
        [-4, -1, -1, 0, 1, 2],
        [[-1, -1, 2], [-1, 0, 1]],
    ),
    (
        [1, 2, 3],
        [],
    ),
    (
        [0, 0, 0, 0],
        [[0, 0, 0]],  # only one unique triplet despite four zeros
    ),
    (
        [-2, -2, 0, 1, 1, 2, 2],
        [[-2, 0, 2], [-2, 1, 1]],
    ),
    (
        [-1, 0, 1],
        [[-1, 0, 1]],
    ),
    (
        [3, 0, -2, -1, 1, 2],
        [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]],
    ),
])
def test_three_sum(nums: list[int], expected: list[list[int]]):
    """
    Parametrized test. Both actual and expected are normalized before comparison.

    Args:
        nums (list[int]): Input array.
        expected (list[list[int]]): Expected set of zero-sum triplets.
    """
    assert normalize(three_sum(nums)) == normalize(expected)
