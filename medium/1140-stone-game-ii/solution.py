            if (i, m) in memo:
                return memo[(i, m)]

            # Can take everything that remains.
            if i + 2 * m >= n:
                memo[(i, m)] = suffix[i]
                return 0

            if i >= n:
        def dp(i, m):
        memo = {}

            suffix[i] = suffix[i + 1] + piles[i]

        for i in range(n - 1, -1, -1):
        n = len(piles)

        # suffix[i] = sum of piles[i:]
        suffix = [0] * (n + 1)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
