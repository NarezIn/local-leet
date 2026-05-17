# 003 — Valid Parentheses

**Difficulty:** Easy

## Problem

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**.

An input string is valid if:
1. Open brackets must be closed by the **same type** of bracket.
2. Open brackets must be closed in the **correct order**.
3. Every closing bracket has a corresponding open bracket of the same type.

## Examples

**Example 1:**
```
Input:  s = "()"
Output: True
```

**Example 2:**
```
Input:  s = "()[]{}"
Output: True
```

**Example 3:**
```
Input:  s = "(]"
Output: False
```

**Example 4:**
```
Input:  s = "([)]"
Output: False
```

**Example 5:**
```
Input:  s = "{[]}"
Output: True
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of parentheses only: `'()[]{}'`

## Function Signature

```python
def is_valid(s: str) -> bool:
```

## Hints

1. Think about what data structure naturally handles "most recently opened" — a stack is ideal here.
2. When you see a closing bracket, what should be on top of the stack?
3. What should the stack look like at the very end if the string is valid?
