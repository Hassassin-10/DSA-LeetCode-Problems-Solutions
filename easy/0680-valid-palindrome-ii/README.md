# Valid Palindrome II

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s`, return `true` *if the *`s`* can be palindrome after deleting **at most one** character from it*.

 

Original
Python3
**Example 1:**

```
Input: s = "aba"
Output: true

```

**Example 2:**

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

```

**Example 3:**

```
Input: s = "abc"
Output: false

```

 

**Constraints:**

- 1 <= s.length <= 105
- s consists of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 61 ms (beats 39.18%)  
**Memory:** 19.5 MB (beats 37.48%)  
**Submitted:** 2026-11-25T04:12:58.502Z  

```py
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalin(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return ispalin(s[i+1:j+1]) or ispalin(s[i:j])
            i += 1
            j -= 1
        return True
```

---

[View on LeetCode](https://leetcode.com/problems/valid-palindrome-ii/)