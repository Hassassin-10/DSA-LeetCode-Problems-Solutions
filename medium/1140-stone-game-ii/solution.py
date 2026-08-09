            # Current player can take X piles.
            # After that, the opponent gets dp(next_i, next_m).
            # Therefore current player's final amount is:
            #
            # total remaining - opponent's best amount
            best = 0

            for x in range(1, min(2 * m, n - i) + 1):
                next_i = i + x
                next_m = max(m, x)

                best = max(
                    best,
                    suffix[i] - dp(next_i, next_m)
                )

            memo[(i, m)] = best
            return best

        return dp(0, 1)
