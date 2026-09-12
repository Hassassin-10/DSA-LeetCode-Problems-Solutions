
        for k in range(1, 5):
            for i in range(1, n + 1):
                # Don't take arr[i - 1].
                best = dp[k][i - 1]

                # Take arr[i - 1].
                j = prev[i - 1] + 1  # dp index corresponding to prev interval
                old_score, old_indices = dp[k - 1][j]

                new_state = (
                    old_score + arr[i - 1][2],
                    tuple(sorted(old_indices + (arr[i - 1][3],)))
                )

                best = better(best, new_state)
                dp[k][i] = best

        return list(dp[4][n][1])

