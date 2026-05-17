"""
Solution for 001 — Two Sum.

Fill in the function body below, then run:
    pytest test_solution.py -v
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Return indices of the two numbers in nums that add up to target.

    Uses a hash map to track each number's index as we scan left to right.
    For each element, we check whether its complement (target - element) has
    already been seen. This gives O(n) time and O(n) space.

    Args:
        nums (list[int]): Array of integers.
        target (int): The target sum.

    Returns:
        list[int]: A two-element list [i, j] where nums[i] + nums[j] == target.
    """
    # items that have traversed would be stored in this map.
    # key: num, value: index
    seen = {}
    for i, num in enumerate(nums):
        want = target - num
        if seen.get(want) is not None:
            return [i, seen[want]]
        else:
            seen[num] = i
