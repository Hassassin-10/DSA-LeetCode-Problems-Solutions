class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing = []
        for i in range(nums[0],nums[-1]+1):
            if i not in nums:
                missing.append(i)
        return missing
