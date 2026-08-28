# Lexicographically Smallest Palindromic Permutation Greater Than Target

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given two strings s and target, each of length n, consisting of lowercase English letters.

Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

 
Example 1:


Input: s = "baba", target = "abba"

Output: "baab"

Explanation:


	The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
	The lexicographically smallest permutation that is strictly greater than target is "baab".



Example 2:


Input: s = "baba", target = "bbaa"

Output: ""

Explanation:


	The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
	None of them is lexicographically strictly greater than target. Therefore, the answer is "".



Example 3:


Input: s = "abc", target = "abb"

Output: ""

Explanation:

s has no palindromic permutations. Therefore, the answer is "".


Example 4:


Input: s = "aac", target = "abb"

Output: "aca"

Explanation:


	The only palindromic permutation of s is "aca".
	"aca" is strictly greater than target. Therefore, the answer is "aca".



 
Constraints:


	1 <= n == s.length == target.length <= 300
	s and target consist of only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 100.00%)  
**Memory:** 19.3 MB (beats 90.91%)  
**Submitted:** 2026-08-28T15:56:48.903Z  

```py
class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        cnt = Counter(s)

        # Check whether a palindrome can be formed.
        odd = [c for c in cnt if cnt[c] % 2]
        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Build the smallest possible left half.
        left = []
        for c in sorted(cnt):
            left.extend([c] * (cnt[c] // 2))

        # Given a left half, construct the full palindrome.
        def palindrome(left):
            return "".join(left) + middle + "".join(left[::-1])

        # We need the first palindrome strictly greater than target.
        #
        # Iterate through possible left halves in lexicographical order.
        # Instead of generating all permutations, find the smallest
        # permutation whose palindrome is > target.

        m = len(left)

        # Find the first left half >= target[:m].
        # If equal, the middle/right half determines whether it is > target.
        target_left = target[:m]

        # Standard "smallest multiset permutation >= target_left".
        def next_geq(target_left):
            a = left[:]

            # Try to construct target_left exactly.
            used = [0] * 26
            for c in a:
                used[ord(c) - 97] += 1

            prefix = []

            for i in range(m):
                t = ord(target_left[i]) - 97

                # Exact match is possible.
                if used[t] > 0:
                    prefix.append(chr(t + 97))
                    used[t] -= 1
                    continue

                # We cannot match target here.
                # Pick the smallest available character > target.
                for x in range(t + 1, 26):
                    if used[x] > 0:
                        prefix.append(chr(x + 97))
                        used[x] -= 1

                        for y in range(26):
                            prefix.extend([chr(y + 97)] * used[y])

                        return prefix

                # No larger character here: backtrack below.
                break

            else:
                # Exact target_left is possible.
                candidate = prefix
                p = palindrome(candidate)

                if p > target:
                    return candidate

            # Backtrack.
            for i in range(len(prefix) - 1, -1, -1):
                old = ord(prefix[i]) - 97
                used[old] += 1

                for x in range(old + 1, 26):
                    if used[x] > 0:
                        result = prefix[:i] + [chr(x + 97)]
                        used[x] -= 1

                        for y in range(26):
                            result.extend([chr(y + 97)] * used[y])

                        return result

            return None

        ans = next_geq(target_left)

        if ans is None:
            return ""

        result = palindrome(ans)

        return result if result > target else ""

```

---

[View on LeetCode](https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/)