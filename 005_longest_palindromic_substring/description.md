# 005 — Longest Palindromic Substring

**Difficulty:** Medium

## Problem

Given a string `s`, return the **longest palindromic substring** in `s`.

A **palindrome** is a string that reads the same forwards and backwards.
A **substring** is a contiguous (non-empty) sequence of characters within a string.

If there are multiple answers of the same maximum length, any one of them is accepted.

## Examples

**Example 1:**
```
Input:  s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2:**
```
Input:  s = "cbbd"
Output: "bb"
```

**Example 3:**
```
Input:  s = "racecar"
Output: "racecar"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

## Function Signature

```python
def longest_palindrome(s: str) -> str:
```

## Hints

1. Brute force: check every substring. That's O(n³) — can you do better?
2. **Expand around center**: for each character (and each gap between characters), expand outward as long as both sides match.
3. There are `2n - 1` possible centers (n characters + n-1 gaps). Each expansion is O(n), giving O(n²) overall.
4. Dynamic programming is another valid approach: `dp[i][j]` = True if `s[i..j]` is a palindrome.
