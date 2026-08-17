                elif left_sum > right_sum:
                    dp[l][r] = max(dp[l][r], right_sum + dp[k + 1][r])
                else:
                    dp[l][r] = max(
                        dp[l][r],
                        left_sum + max(dp[l][k], dp[k + 1][r])
                    )

                # Also check the split immediately before k.
                if k > l:
                    left_sum = range_sum(l, k - 1)
                    right_sum = total - left_sum

                    # Here left_sum < right_sum.
                    dp[l][r] = max(
                        dp[l][r],
                        left_sum + dp[l][k - 1]
                    )

        return dp[0][n - 1]
