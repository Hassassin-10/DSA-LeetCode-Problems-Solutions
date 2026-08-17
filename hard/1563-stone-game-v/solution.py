from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score obtainable from stoneValue[l:r+1]
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                for k in range(l, r):
                    left = prefix[k + 1] - prefix[l]
                    right = prefix[r + 1] - prefix[k + 1]

                    if left < right:
                        # Bob throws away right
                        dp[l][r] = max(
                            dp[l][r],
                            left + dp[l][k]
                        )

                    elif left > right:
                        # Bob throws away left
                        dp[l][r] = max(
                            dp[l][r],
                            right + dp[k + 1][r]
                        )

                    else:
                        # Equal: Alice chooses either side
                        dp[l][r] = max(
                            dp[l][r],
                            left + dp[l][k],
                            right + dp[k + 1][r]
                        )

        return dp[0][n - 1]