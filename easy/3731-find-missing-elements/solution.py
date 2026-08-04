class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        rem = []
        sort = nums.sort()
        min = nums[0]
        max = nums[-1]
        for i in range(min,max):
            pre = i - 1
            if cur - pre > 1:
                rem = [cur]
            cur = i
        return rem

