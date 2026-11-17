# Peak Index in a Mountain Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer **mountain** array `arr` of length `n` where the values increase to a **peak element** and then decrease.

Return the index of the peak element.

Your task is to solve it in `O(log(n))` time complexity.

 

Original
Python3
**Example 1:**

**Input:** arr = [0,1,0]

**Output:** 1

**Example 2:**

**Input:** arr = [0,2,1,0]

**Output:** 1

**Example 3:**

**Input:** arr = [0,10,5,2]

**Output:** 1

 

**Constraints:**

- 3 <= arr.length <= 105
- 0 <= arr[i] <= 106
- arr is guaranteed to be a mountain array.

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 31.3 MB (beats 43.27%)  
**Submitted:** 2026-11-17T11:04:57.892Z  

```py
class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start , end = 0,len(arr)-2
        while start < end:
            mid = (start+end)//2
            if(arr[mid] > arr[mid+1]):
                end=mid
            else:
                start=mid+1
        return start
```

---

[View on LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/)