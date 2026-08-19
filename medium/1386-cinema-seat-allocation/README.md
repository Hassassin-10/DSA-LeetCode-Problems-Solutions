# Cinema Seat Allocation

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.

A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:


	seats 2, 3, 4, 5
	seats 4, 5, 6, 7
	seats 6, 7, 8, 9


A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

Return an integer denoting the maximum number of four-person groups that can be assigned.

 
Example 1:



Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.


Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2


Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4


 
Constraints:


	1 <= n <= 109
	1 <= reservedSeats.length <= min(10 * n, 104)
	reservedSeats[i] == [rowi, seati]
	1 <= rowi <= n
	1 <= seati <= 10
	All reservedSeats[i] are distinct.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.3 MB  
**Submitted:** 2026-08-19T15:37:52.747Z  

```py

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << s)

        # Every completely free row can accommodate 2 groups.
        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = (mask & ((1 << 2) | (1 << 3) | (1 << 4) | (1 << 5))) == 0
            middle = (mask & ((1 << 4) | (1 << 5) | (1 << 6) | (1 << 7))) == 0
            right = (mask & ((1 << 6) | (1 << 7) | (1 << 8) | (1 << 9))) == 0

            if left and right:
                # Both non-overlapping blocks can be used.
                ans += 2
            elif left or middle or right:
                # At least one valid block exists.
                ans += 1

        return ans

```

---

[View on LeetCode](https://leetcode.com/problems/cinema-seat-allocation/)