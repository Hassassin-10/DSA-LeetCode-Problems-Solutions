# Valid Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`* if it is a **palindrome**, or *`false`* otherwise*.

 

Original
Python3
**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

**Example 3:**

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

**Constraints:**

- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 17 ms (beats 6.55%)  
**Memory:** 19.6 MB (beats 70.83%)  
**Submitted:** 2026-11-24T07:48:53.976Z  

```py

class Solution:
    def filter(self, s):
        st = ""
        for i in range(len(s)):
            if "A" <= s[i] <= "Z":
                st += chr(ord(s[i]) + 32)
            elif "a" <= s[i] <= "z" or "0" <= s[i] <= "9":
                st += s[i]
        return st

    def isPalindrome(self, s: str) -> bool:
        f = self.filter(s)
        i, j = 0, len(f) - 1

        while i < j:
            if f[i] != f[j]:
                return False
            i += 1
            j -= 1

        return True

```

---

[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)