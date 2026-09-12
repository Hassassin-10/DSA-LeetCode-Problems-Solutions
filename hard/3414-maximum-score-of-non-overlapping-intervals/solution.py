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
