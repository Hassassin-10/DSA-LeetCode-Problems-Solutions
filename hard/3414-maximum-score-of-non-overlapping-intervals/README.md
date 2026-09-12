# Maximum Score of Non-overlapping Intervals

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 
Example 1:


Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.


Example 2:


Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.


 
Constraints:


	1 <= intevals.length <= 5 * 104
	intervals[i].length == 3
	intervals[i] = [li, ri, weighti]
	1 <= li <= ri <= 109
	1 <= weighti <= 109

## Solution

**Language:** Python  
**Runtime:** 1473 ms (beats 62.71%)  
**Memory:** 75.3 MB (beats 61.02%)  
**Submitted:** 2026-09-12T15:32:30.734Z  

```py
from typing import List
from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # [left, right, weight, original_index]
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by right endpoint.
        arr.sort(key=lambda x: x[1])

        # Ends of sorted intervals.
        ends = [x[1] for x in arr]

        # prev[i] = number of intervals ending before arr[i] starts.
        #
        # Because intervals sharing a boundary overlap, we need:
        # previous right < current left
        prev = [
            bisect_left(ends, arr[i][0]) - 1
            for i in range(n)
        ]

        # dp[k][i] = best (score, tuple of indices)
        # using the first i intervals, with at most k selected.
        #
        # We use 1-based i for convenience.
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        def better(a, b):
            """Return the better of two (score, tuple) states."""
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # Same score -> lexicographically smaller indices.
            return a if a[1] < b[1] else b

        for k in range(1, 5):
            for i in range(1, n + 1):
                # Don't take arr[i - 1].
                best = dp[k][i - 1]

                # Take arr[i - 1].
                j = prev[i - 1] + 1  # dp index corresponding to prev interval
                old_score, old_indices = dp[k - 1][j]

                new_state = (
                    old_score + arr[i - 1][2],
                    tuple(sorted(old_indices + (arr[i - 1][3],)))
                )

                best = better(best, new_state)
                dp[k][i] = best

        return list(dp[4][n][1])

```

---

[View on LeetCode](https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/)