# 008 — Group Anagrams

**Difficulty:** Medium

## Problem

Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.

Two strings are anagrams of each other if one can be rearranged to form the other (they contain the same characters with the same frequencies).

## Examples

**Example 1:**
```
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
Explanation: "eat", "tea", and "ate" are anagrams of each other.
             "tan" and "nat" are anagrams of each other.
             "bat" has no anagram partner.
```

**Example 2:**
```
Input:  strs = [""]
Output: [[""]]
```

**Example 3:**
```
Input:  strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters only.

## Function Signature

```python
def group_anagrams(strs: list[str]) -> list[list[str]]:
```

## Hints

1. What property is the same for all anagrams of a word? Think about what makes a good hash key.
2. Sorting the characters of a word gives a canonical form — `"eat"` → `"aet"`, `"tea"` → `"aet"`. Use that as the dictionary key.
3. Alternatively, use a tuple of 26 character counts as the key (avoids sorting).
