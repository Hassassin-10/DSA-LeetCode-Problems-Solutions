class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        start , end = 0,len(arr)-2
        while start < end:
            mid = (start+end)//2
            if(arr[mid] > arr[mid+1]):
                end=mid
            else:
                start=mid+1
        return start