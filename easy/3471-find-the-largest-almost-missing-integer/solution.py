class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        # Count how many size-k subarrays contain each number.
        for i in range(len(nums) - k + 1):
            seen = set(nums[i:i + k])

            for x in seen:
                count[x] = count.get(x, 0) + 1

        # Largest number that appears in exactly one subarray.
        ans = -1
        for x, freq in count.items():
            if freq == 1:
                ans = max(ans, x)

        return ans