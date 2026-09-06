# Distinct Subsequences

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 
Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit


Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

 
Constraints:


	1 <= s.length, t.length <= 1000
	s and t consist of English letters.

## Solution

**Language:** Python  
**Runtime:** 232 ms (beats 81.37%)  
**Memory:** 19.5 MB (beats 91.77%)  
**Submitted:** 2026-09-06T16:56:17.997Z  

```py
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[j] = number of ways to form t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string can always be formed

        for ch in s:
            for j in range(n, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]

```

---

[View on LeetCode](https://leetcode.com/problems/distinct-subsequences/)