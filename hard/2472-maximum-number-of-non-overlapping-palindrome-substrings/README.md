# Maximum Number of Non-overlapping Palindrome Substrings

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a string `s` and a **positive** integer `k`.

Select a set of **non-overlapping** substrings from the string `s` that satisfy the following conditions:

- The length of each substring is at least k.
- Each substring is a palindrome.

Return *the **maximum** number of substrings in an optimal selection*.

A **substring** is a contiguous sequence of characters within a string.

 

**Example 1:**

```
Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

```

**Example 2:**

```
Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

```

 

**Constraints:**

- 1 <= k <= s.length <= 2000
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 1984 ms (beats 28.86%)  
**Memory:** 50.5 MB (beats 30.41%)  
**Submitted:** 2026-09-15T13:49:32.058Z  

```py
class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = maximum number of valid palindromes
        # in s[:i]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Don't end a palindrome at i - 1
            dp[i] = dp[i - 1]

            # Try every palindrome ending at i - 1
            for j in range(i - k + 1):
                if pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]

```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)