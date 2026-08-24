class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # prefix[i] = sum of stones[0:i]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # If Alice takes all n stones immediately.
        best = prefix[n]

        # Consider taking the first i stones, i >= 2.
        # The opponent then plays optimally on the remaining game.
        for i in range(n - 1, 1, -1):
            best = max(best, prefix[i] - best)

        return best