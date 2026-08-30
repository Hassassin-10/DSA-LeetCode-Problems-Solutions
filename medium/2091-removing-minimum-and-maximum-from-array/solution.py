        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Put smaller index first
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 1. Remove both from the front
        front = right + 1

        # 2. Remove both from the back
        back = n - left

        # 3. Remove left from front, right from back
        both = (left + 1) + (n - right)

        return min(front, back, both)
    def minimumDeletions(self, nums: List[int]) -> int:
class Solution:
