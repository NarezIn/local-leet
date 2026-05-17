# 002 — Palindrome Number

**Difficulty:** Easy

## Problem

Given an integer `x`, return `True` if `x` is a **palindrome**, and `False` otherwise.

A number is a palindrome when it reads the same forwards and backwards.

## Examples

**Example 1:**
```
Input:  x = 121
Output: True
Explanation: 121 reads the same from left to right and right to left.
```

**Example 2:**
```
Input:  x = -121
Output: False
Explanation: From left to right it reads -121. From right to left it reads 121-.
```

**Example 3:**
```
Input:  x = 10
Output: False
Explanation: From right to left it reads 01, which is not 10.
```

## Constraints

- `-2^31 <= x <= 2^31 - 1`

## Function Signature

```python
def is_palindrome(x: int) -> bool:
```

## Hints

1. Are negative numbers ever palindromes?
2. The easy approach: convert to a string and compare it to its reverse.
3. Challenge: can you solve it without converting to a string? Try reversing only the second half of the number.
