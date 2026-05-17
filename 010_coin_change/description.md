# 010 — Coin Change

**Difficulty:** Medium

## Problem

You are given an integer array `coins` representing coin denominations and an integer `amount` representing a total amount of money.

Return the **fewest number of coins** needed to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an **infinite number** of each kind of coin.

## Examples

**Example 1:**
```
Input:  coins = [1, 5, 10, 25], amount = 36
Output: 3
Explanation: 25 + 10 + 1 = 36 using 3 coins.
```

**Example 2:**
```
Input:  coins = [2], amount = 3
Output: -1
Explanation: 3 cannot be formed using only 2-cent coins.
```

**Example 3:**
```
Input:  coins = [1], amount = 0
Output: 0
Explanation: Zero coins needed to make amount 0.
```

**Example 4:**
```
Input:  coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 5 + 5 + 1 = 11.
```

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Function Signature

```python
def coin_change(coins: list[int], amount: int) -> int:
```

## Hints

1. This is a classic **dynamic programming** problem.
2. Define `dp[i]` as the minimum number of coins to make amount `i`. What is `dp[0]`?
3. For each amount `i` from 1 to `amount`, try every coin `c`. If `i - c >= 0` and `dp[i - c]` is reachable, then `dp[i] = min(dp[i], dp[i - c] + 1)`.
4. Initialize `dp[i] = infinity` (or `amount + 1`) to represent "not yet reachable".
