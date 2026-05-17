# 001 — Two Sum

**Difficulty:** Easy

## Problem

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.

You may assume that each input has **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

## Examples

**Example 1:**
```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] == 9
```

**Example 2:**
```
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]
```

**Example 3:**
```
Input:  nums = [3, 3], target = 6
Output: [0, 1]
```

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Exactly one valid answer exists.

## Function Signature

```python
def two_sum(nums: list[int], target: int) -> list[int]:
```

## Hints

1. A brute force approach checks every pair — what is its time complexity?
2. Can you use a hash map to bring it down to O(n)?
3. As you iterate, ask: "have I already seen the complement of this number?"
