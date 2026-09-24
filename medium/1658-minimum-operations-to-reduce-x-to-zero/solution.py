class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        # We need to remove everything if target == 0
        if target == 0:
            return n

        # If target < 0, x is greater than the total sum
        if target < 0:
            return -1

        left = 0
        window_sum = 0
        max_len = -1

        for right in range(n):
            window_sum += nums[right]

            # Shrink window until its sum <= target
            while window_sum > target and left <= right:
                window_sum -= nums[left]
                left += 1

            # Found a valid subarray
            if window_sum == target:
                max_len = max(max_len, right - left + 1)

        return -1 if max_len == -1 else n - max_len
