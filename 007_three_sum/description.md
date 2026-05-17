# 007 — 3Sum

**Difficulty:** Medium

## Problem

Given an integer array `nums`, return all **unique** triplets `[nums[i], nums[j], nums[k]]` such that:
- `i`, `j`, and `k` are distinct indices.
- `nums[i] + nums[j] + nums[k] == 0`

The solution set must **not** contain duplicate triplets.

## Examples

**Example 1:**
```
Input:  nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: Both triplets sum to zero. The order of the output does not matter.
```

**Example 2:**
```
Input:  nums = [0, 1, 1]
Output: []
Explanation: No triplet sums to zero.
```

**Example 3:**
```
Input:  nums = [0, 0, 0]
Output: [[0, 0, 0]]
```

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Function Signature

```python
def three_sum(nums: list[int]) -> list[list[int]]:
```

## Hints

1. Sort the array first. This makes it easy to skip duplicates and use two pointers.
2. Fix one element `nums[i]`, then reduce the problem to **Two Sum** on the remaining sorted subarray.
3. Use left and right pointers starting from `i+1` and `len(nums)-1`. Move them based on whether the sum is too large or too small.
4. After finding a valid triplet, advance both pointers and skip over duplicates.
