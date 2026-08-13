# Longest Substring of One Repeating Character

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 
Example 1:

Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
Output: [3,3,4]
Explanation: 
- 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
- 2nd query updates s = "bbbccc". 
  The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
- 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
Thus, we return [3,3,4].


Example 2:

Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
Output: [2,3]
Explanation:
- 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.
- 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
Thus, we return [2,3].


 
Constraints:


	1 <= s.length <= 105
	s consists of lowercase English letters.
	k == queryCharacters.length == queryIndices.length
	1 <= k <= 105
	queryCharacters consists of lowercase English letters.
	0 <= queryIndices[i] < s.length

## Solution

**Language:** Python  
**Runtime:** 2554 ms (beats 73.77%)  
**Memory:** 138.4 MB (beats 13.12%)  
**Submitted:** 2026-08-13T08:22:36.923Z  

```py
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)

        # Each node:
        # [length, left_char, right_char, left_len, right_len, best]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            length1, lc1, rc1, ll1, rl1, best1 = a
            length2, lc2, rc2, ll2, rl2, best2 = b

            length = length1 + length2
            left_char = lc1
            right_char = rc2

            # Length of prefix consisting of the same character
            left_len = ll1
            if ll1 == length1 and rc1 == lc2:
                left_len += ll2

            # Length of suffix consisting of the same character
            right_len = rl2
            if rl2 == length2 and rc1 == lc2:
                right_len += rl1

            # Best run completely inside either segment
            best = max(best1, best2)

            # Best run crossing the boundary
            if rc1 == lc2:
                best = max(best, rl1 + ll2)

            return (
                length,
                left_char,
                right_char,
                left_len,
                right_len,
                best
            )

        def build(node, l, r):
            if l == r:
                tree[node] = (1, s[l], s[l], 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, char):
            if l == r:
                tree[node] = (1, char, char, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][5])

        return ans
```

---

[View on LeetCode](https://leetcode.com/problems/longest-substring-of-one-repeating-character/)