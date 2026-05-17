# 006 — Container With Most Water

**Difficulty:** Medium

## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that holds the **most water**. Return the **maximum amount of water** a container can store.

**Note:** You may not slant the container.

The amount of water between lines at index `i` and `j` (where `i < j`) is:
```
water = (j - i) * min(height[i], height[j])
```

## Examples

**Example 1:**
```
Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
Output: 49
Explanation: Lines at index 1 (height 8) and index 8 (height 7).
             Water = (8 - 1) * min(8, 7) = 7 * 7 = 49.
```

**Example 2:**
```
Input:  height = [1, 1]
Output: 1
```

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Function Signature

```python
def max_area(height: list[int]) -> int:
```

## Hints

1. Brute force: try every pair `(i, j)`. That's O(n²) — aim for O(n).
2. Place one pointer at each end. The water is limited by the **shorter** line.
3. Moving the pointer at the taller line inward can only decrease the width and won't help — so always move the pointer at the **shorter** line.
