# Smallest Palindromic Rearrangement II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a palindromic string s and an integer k.

Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.

Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

 
Example 1:


Input: s = "abba", k = 2

Output: "baab"

Explanation:


	The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
	Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".



Example 2:


Input: s = "aa", k = 2

Output: ""

Explanation:


	There is only one palindromic rearrangement: "aa".
	The output is an empty string since k = 2 exceeds the number of possible rearrangements.



Example 3:


Input: s = "bacab", k = 1

Output: "abcba"

Explanation:


	The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
	Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".



 
Constraints:


	1 <= s.length <= 104
	s consists of lowercase English letters.
	s is guaranteed to be palindromic.
	1 <= k <= 106

## Solution

**Language:** Python  
**Runtime:** 1228 ms (beats 29.58%)  
**Memory:** 19.9 MB (beats 57.75%)  
**Submitted:** 2026-07-29T17:36:08.340Z  

```py
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from collections import Counter
        import math

        freq = Counter(s)
        half = {}
        mid = ""
        m = 0

        for char in "abcdefghijklmnopqrstuvwxyz":
            if freq[char] > 0:
                if freq[char] % 2 != 0:
                    mid += char
                half[char] = freq[char] // 2
                m += half[char]

        def get_ways(f, target_k):
            ways = 1
            curr_len = 0
            for char in "abcdefghijklmnopqrstuvwxyz":
                count = f.get(char, 0)
                if count > 0:
                    curr_len += count
                    ways *= math.comb(curr_len, count)
                    if ways > target_k:
                        return target_k + 1
            return ways

        if get_ways(half, k) < k:
            return ""

        first_half = []
        for _ in range(m):
            for char in "abcdefghijklmnopqrstuvwxyz":
                if half.get(char, 0) > 0:
                    half[char] -= 1
                    ways = get_ways(half, k)

                    if ways >= k:
                        first_half.append(char)
                        break
                    else:
                        k -= ways
                        half[char] += 1

        first_str = "".join(first_half)
        return first_str + mid + first_str[::-1]

```

---

[View on LeetCode](https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/)