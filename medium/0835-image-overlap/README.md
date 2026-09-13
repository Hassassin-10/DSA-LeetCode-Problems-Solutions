# Image Overlap

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

 
Example 1:

Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).



Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1


Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0


 
Constraints:


	n == img1.length == img1[i].length
	n == img2.length == img2[i].length
	1 <= n <= 30
	img1[i][j] is either 0 or 1.
	img2[i][j] is either 0 or 1.

## Solution

**Language:** Python  
**Runtime:** 243 ms (beats 60.84%)  
**Memory:** 19.7 MB (beats 50.00%)  
**Submitted:** 2026-09-13T06:30:18.552Z  

```py
from typing import List
from collections import Counter

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        ones1 = []
        ones2 = []

        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones1.append((r, c))
                if img2[r][c] == 1:
                    ones2.append((r, c))

        shifts = Counter()

        # If img1's (r1, c1) is moved to img2's (r2, c2),
        # the required translation is (r2-r1, c2-c1).
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2 - c1)
                shifts[shift] += 1

        return max(shifts.values(), default=0)

```

---

[View on LeetCode](https://leetcode.com/problems/image-overlap/)