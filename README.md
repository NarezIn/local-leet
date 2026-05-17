# Local LeetCode Practice

10 LeetCode-style problems for offline practice.

## Structure

Each problem lives in its own subdirectory:
- `description.md` — problem statement, examples, constraints
- `solution.py` — your solution goes here (fill in the function body)
- `test_solution.py` — pytest test cases that validate your solution

## How to start

TODO: Write this part later.

## How to run tests

From within a problem directory:
```
cd 001_two_sum
pytest test_solution.py -v
```

Or run all problems from the root:
```
pytest -v
```

## Problems

| # | Title | Difficulty |
|---|-------|------------|
| 001 | Two Sum | Easy |
| 002 | Palindrome Number | Easy |
| 003 | Valid Parentheses | Easy |
| 004 | Longest Substring Without Repeating Characters | Medium |
| 005 | Longest Palindromic Substring | Medium |
| 006 | Container With Most Water | Medium |
| 007 | 3Sum | Medium |
| 008 | Group Anagrams | Medium |
| 009 | Product of Array Except Self | Medium |
| 010 | Coin Change | Medium |

## Tips

- Read `description.md` carefully before writing any code.
- Try to solve it on your own before looking up hints.
- Run `pytest test_solution.py -v` often to see which cases pass.
- All test files import from `solution.py` in the same directory.
