# Maximum Number of Non-Overlapping Substrings

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given a string `s` of lowercase letters, you need to find the maximum number of **non-empty** substrings of `s` that meet the following conditions:

- The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
- A substring that contains a certain character c must also contain all occurrences of c.

Find *the maximum number of substrings that meet the above conditions*. If there are multiple solutions with the same number of substrings, *return the one with minimum total length. *It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in **any** order.

 

**Example 1:**

```
Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

```

**Example 2:**

```
Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

```

 

**Constraints:**

- 1 <= s.length <= 105
- s contains only lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 183 ms (beats 75.66%)  
**Memory:** 20.3 MB (beats 70.80%)  
**Submitted:** 2026-09-18T07:09:56.505Z  

```py
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Track the first and last occurrence of each character
        left = {}
        right = {}
        for i, char in enumerate(s):
            if char not in left:
                left[char] = i
            right[char] = i

        valid_intervals = []

        # Step 2: For each character, try to find a valid self-contained substring interval
        for char in left:
            l = left[char]
            r = right[char]
            is_valid = True
            
            i = l
            while i <= r:
                curr_char = s[i]
                # If a character inside expands left before 'l', then 'l' is invalid
                if left[curr_char] < l:
                    is_valid = False
                    break
                # Expand right boundary to include all occurrences of 'curr_char'
                r = max(r, right[curr_char])
                i += 1
            
            if is_valid:
                valid_intervals.append((l, r))

        # Step 3: Sort candidate intervals by their end index (Greedy choice)
        valid_intervals.sort(key=lambda x: x[1])

        result = []
        last_end = -1

        for l, r in valid_intervals:
            # Pick non-overlapping intervals
            if l > last_end:
                result.append(s[l : r + 1])
                last_end = r

        return result
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/)