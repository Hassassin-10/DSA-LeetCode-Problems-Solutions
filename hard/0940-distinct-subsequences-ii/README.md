# Distinct Subsequences II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
 
Example 1:

Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".


Example 2:

Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".


Example 3:

Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".


 
Constraints:


	1 <= s.length <= 2000
	s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.2 MB  
**Submitted:** 2026-09-07T14:13:30.277Z  

```py
        # last[c] = number of distinct subsequences that existed
        # before the previous occurrence of character c
        last = [0] * 26

        for ch in s:
            c = ord(ch) - ord('a')

            # Every existing subsequence can append ch,
            # and ch itself forms a new subsequence.
            new_dp = (2 * dp + 1 - last[c]) % MOD

            # Save the old dp value for this character.
            last[c] = dp + 1

        dp = 0
        # after processing s[:i]
        # dp[i] = number of distinct non-empty subsequences

        MOD = 10**9 + 7
    def distinctSubseqII(self, s: str) -> int:
class Solution:

```

---

[View on LeetCode](https://leetcode.com/problems/distinct-subsequences-ii/)