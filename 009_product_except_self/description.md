# 009 — Product of Array Except Self

**Difficulty:** Medium

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the **product of all elements of `nums` except `nums[i]`**.

The product of any prefix or suffix of `nums` is **guaranteed to fit** in a 32-bit integer.

**You must write an algorithm that runs in O(n) time and without using the division operation.**

## Examples

**Example 1:**
```
Input:  nums = [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Explanation:
  answer[0] = 2 * 3 * 4 = 24
  answer[1] = 1 * 3 * 4 = 12
  answer[2] = 1 * 2 * 4 = 8
  answer[3] = 1 * 2 * 3 = 6
```

**Example 2:**
```
Input:  nums = [-1, 1, 0, -3, 3]
Output: [0, 0, 9, 0, 0]
```

## Constraints

- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix fits in a 32-bit integer.

## Follow-up

Can you solve it using O(1) extra space (the output array does not count)?

## Function Signature

```python
def product_except_self(nums: list[int]) -> list[int]:
```

## Hints

1. Why is division disallowed? Think about what happens when an element is 0.
2. For each index `i`, the answer is `(product of all elements to the LEFT of i) * (product of all elements to the RIGHT of i)`.
3. Compute a **prefix product** array (left-to-right), then multiply by a running **suffix product** (right-to-left) in a second pass.
