class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        xor = 0

        for num in nums:
            xor ^= num

        if xor != 0:
            return len(nums)

        # Total XOR is 0.
        # If there's a non-zero element, remove it.
        for num in nums:
            if num != 0:
                return len(nums) - 1

        # All elements are zero.
        return 0
