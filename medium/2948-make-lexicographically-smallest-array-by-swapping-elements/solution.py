from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # (value, original index), sorted by value
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = nums[:]
        start = 0

        for end in range(1, n + 1):
            # End the current connected group if there is a large gap.
            if end == n or arr[end][0] - arr[end - 1][0] > limit:
                # Values in this group are already sorted.
                values = [arr[i][0] for i in range(start, end)]

                # These values can be assigned to any indices in the group.
                indices = sorted(arr[i][1] for i in range(start, end))

                for idx, value in zip(indices, values):
                    ans[idx] = value

                start = end

        return ans
