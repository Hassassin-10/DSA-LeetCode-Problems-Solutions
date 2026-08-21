# Kth Smallest Amount With Single Denomination Combination

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

 
Example 1:


Input: coins = [3,6,9], k = 3

Output:  9

Explanation: The given coins can make the following amounts:
Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.
All of the coins combined produce: 3, 6, 9, 12, 15, etc.


Example 2:


Input: coins = [5,2], k = 7

Output: 12 

Explanation: The given coins can make the following amounts:
Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.


 
Constraints:


	1 <= coins.length <= 15
	1 <= coins[i] <= 25
	1 <= k <= 2 * 109
	coins contains pairwise distinct integers.

## Solution

**Language:** Python  
**Runtime:** 95 ms (beats 58.54%)  
**Memory:** 19.4 MB (beats 93.90%)  
**Submitted:** 2026-08-21T15:38:57.168Z  

```py
from typing import List
from math import gcd


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove redundant coins:
        # if a coin is a multiple of another coin, its multiples
        # are already covered by the smaller coin.
        coins.sort()
        filtered = []

        for c in coins:
            if not any(c % x == 0 for x in filtered):
                filtered.append(c)

        coins = filtered
        n = len(coins)

        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b

        def count(x: int) -> int:
            """Number of distinct amounts <= x."""
            total = 0

            # Inclusion-exclusion over all subsets.
            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        cur_lcm = lcm(cur_lcm, coins[i])

                        # No need to continue if LCM > x.
                        if cur_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                multiples = x // cur_lcm

                if bits & 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        # The answer is at most min(coins) * k.
        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo
```

---

[View on LeetCode](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/)