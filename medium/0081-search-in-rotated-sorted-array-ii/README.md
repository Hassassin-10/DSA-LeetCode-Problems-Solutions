# Search in Rotated Sorted Array II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true`* if *`target`* is in *`nums`*, or *`false`* if it is not in *`nums`*.*

You must decrease the overall operation steps as much as possible.

 

Original
Python3
**Example 1:**

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

```

**Example 2:**

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

```

 

**Constraints:**

- 1 <= nums.length <= 5000
- -104 <= nums[i] <= 104
- nums is guaranteed to be rotated at some pivot.
- -104 <= target <= 104

 

**Follow up:** This problem is similar to Search in Rotated Sorted Array, but `nums` may contain **duplicates**. Would this affect the runtime complexity? How and why?

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 19.5 MB (beats 58.64%)  
**Submitted:** 2026-11-17T10:30:55.608Z  

```py
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start , end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1
                continue
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid+1] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
```

---

[View on LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)