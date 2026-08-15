# Maximum Length Substring With Two Occurrences

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 
Example 1:


Input: s = "bcbbbcba"

Output: 4

Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:


Input: s = "aaaa"

Output: 2

Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

 
Constraints:


	2 <= s.length <= 100
	s consists only of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 46.53%)  
**Memory:** 19.2 MB (beats 60.15%)  
**Submitted:** 2026-08-15T09:11:41.102Z  

```py
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            # Shrink window until every character occurs at most twice
            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/)