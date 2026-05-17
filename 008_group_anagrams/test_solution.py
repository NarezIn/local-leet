"""
Test cases for 008 — Group Anagrams.

Order within each group and order of groups in the result both don't matter,
so each test normalizes both sides before comparing.

Run with:
    pytest test_solution.py -v
"""

import pytest
from solution import group_anagrams


def normalize(groups: list[list[str]]) -> list[list[str]]:
    """
    Produce a canonical form for comparison: sort each group, then sort the list of groups.

    Args:
        groups (list[list[str]]): Raw output from the solution.

    Returns:
        list[list[str]]: Sorted groups in sorted order.
    """
    return sorted(sorted(g) for g in groups)


@pytest.mark.parametrize("strs, expected", [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    (
        [""],
        [[""]],
    ),
    (
        ["a"],
        [["a"]],
    ),
    (
        ["ab", "ba", "abc", "bca", "cab", "xyz"],
        [["ab", "ba"], ["abc", "bca", "cab"], ["xyz"]],
    ),
    (
        ["a", "b", "c"],
        [["a"], ["b"], ["c"]],  # no anagrams — every word is its own group
    ),
    (
        ["aaa", "aaa"],
        [["aaa", "aaa"]],  # duplicates go in the same group
    ),
    (
        ["listen", "silent", "enlist", "hello", "world"],
        [["enlist", "listen", "silent"], ["hello"], ["world"]],
    ),
    (
        ["abc", "abc", "abc"],
        [["abc", "abc", "abc"]],
    ),
])
def test_group_anagrams(strs: list[str], expected: list[list[str]]):
    """
    Parametrized test. Both actual and expected are normalized before comparison.

    Args:
        strs (list[str]): Input strings.
        expected (list[list[str]]): Expected anagram groups.
    """
    assert normalize(group_anagrams(strs)) == normalize(expected)
