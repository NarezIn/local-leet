# 004 — Longest Substring Without Repeating Characters

**Difficulty:** Medium

## Problem

Given a string `s`, find the **length** of the longest substring that contains no repeating characters.

A **substring** is a contiguous sequence of characters within a string (unlike a subsequence, you cannot skip characters).

## Examples

**Example 1:**
```
Input:  s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeating characters.
```

**Example 2:**
```
Input:  s = "bbbbb"
Output: 1
Explanation: "b" is the only valid substring; its length is 1.
```

**Example 3:**
```
Input:  s = "pwwkew"
Output: 3
Explanation: "wke" is the answer. Note that "pwke" is a subsequence, not a substring.
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

## Function Signature

```python
def length_of_longest_substring(s: str) -> int:
```

## Hints

1. A brute-force approach checks all substrings. What is its time complexity?
2. Think about a **sliding window**: maintain a window `[left, right]` where all characters are unique.
3. Use a set or dictionary to track characters in the current window. When you hit a duplicate, shrink from the left.
