class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            # No piles left
            if i == n:
                return 0

            if (i, m) in memo:
                return memo[(i, m)]

            # Current player can take X piles.
            # After that, the opponent gets dp(next_i, next_m).
            # Therefore current player's final amount is:
            #
            # total remaining - opponent's best amount
            best = 0

            for x in range(1, min(2 * m, n - i) + 1):
                next_i = i + x
                next_m = max(m, x)

                best = max(
                    best,
                    suffix[i] - dp(next_i, next_m)
                )

            memo[(i, m)] = best
            return best

        return dp(0, 1)