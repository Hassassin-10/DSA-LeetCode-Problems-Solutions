# Lexicographically Smallest Permutation Greater Than Target

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 
Example 1:


Input: s = "abc", target = "bba"

Output: "bca"

Explanation:


	The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
	The lexicographically smallest permutation that is strictly greater than target is "bca".



Example 2:


Input: s = "leet", target = "code"

Output: "eelt"

Explanation:


	The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
	The lexicographically smallest permutation that is strictly greater than target is "eelt".



Example 3:


Input: s = "baba", target = "bbaa"

Output: ""

Explanation:


	The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
	None of them is lexicographically strictly greater than target. Therefore, the answer is "".



 
Constraints:


	1 <= s.length == target.length <= 300
	s and target consist of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 27 ms (beats 23.68%)  
**Memory:** 19.5 MB (beats 42.11%)  
**Submitted:** 2026-08-27T07:24:30.103Z  

```py
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Try to make the answer greater at position i.
        # We go from right to left so that the first difference
        # happens as late as possible.
        for i in range(n - 1, -1, -1):
            # Recreate the available characters after using target[:i]
            rem = cnt[:]

            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if rem[x] == 0:
                    possible = False
                    break

                rem[x] -= 1

            if not possible:
                continue

            # Find the smallest character > target[i]
            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if rem[c] > 0:
                    rem[c] -= 1

                    # target[:i] + chosen larger character
                    ans = target[:i] + chr(ord('a') + c)

                    # Smallest possible suffix
                    for k in range(26):
                        ans += chr(ord('a') + k) * rem[k]

                    return ans

        return ""
```

---

[View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/)