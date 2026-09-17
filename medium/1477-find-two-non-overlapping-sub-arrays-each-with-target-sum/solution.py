class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        
        # best[i] = minimum length of a target-sum subarray
        # completely within arr[0..i]
        INF = n + 1
        best = [INF] * n
        
        left = 0
        curr_sum = 0
        ans = INF
        
        for right in range(n):
            curr_sum += arr[right]
            
            # Since all numbers are positive, shrink from left
            # until curr_sum <= target.
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1
            
            if curr_sum == target:
                length = right - left + 1
                
                # There is a previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])
                
                # Best target-sum subarray seen so far
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)
            else:
                # No subarray ending at right, keep previous best
                if right > 0:
                    best[right] = best[right - 1]
        
        return -1 if ans == INF else ans
