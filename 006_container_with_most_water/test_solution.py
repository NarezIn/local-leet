"""
Test cases for 006 — Container With Most Water.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import max_area


@pytest.mark.parametrize("height, expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # classic example
    ([1, 1],                         1),  # minimum array, equal heights
    ([4, 3, 2, 1, 4],               16),  # symmetric, answer spans full width
    ([1, 2, 1],                      2),  # taller middle doesn't help
    ([1, 2, 4, 3],                   4),  # answer not at endpoints
    ([2, 3, 10, 5, 7, 8, 9],        36),  # tall interior lines
    ([0, 0],                         0),  # zero heights
    ([0, 5],                         0),  # one zero height
    ([10, 10],                      10),  # two equal tall lines
    ([1, 3, 2, 5, 25, 24, 5],       24),  # very tall lines near each other
    ([3, 1, 2, 4, 5],               12),  # increasing heights
    ([5, 4, 3, 2, 1],               12),  # decreasing heights — same as above reversed
])
def test_max_area(height: list[int], expected: int):
    """
    Parametrized test covering various container configurations.

    Args:
        height (list[int]): Input heights.
        expected (int): Expected maximum water area.
    """
    assert max_area(height) == expected
