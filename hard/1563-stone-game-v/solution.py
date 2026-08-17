from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(l, r):
            if l >= r:
                return 0

            ans = 0
            left = 0
            right = prefix[r + 1] - prefix[l]

            for k in range(l, r):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # Alice keeps the left side.
                    #
                    # If left * 2 <= ans, this split cannot
                    # possibly improve the current answer.
                    if left * 2 <= ans:
                        continue

                    ans = max(ans, left + dfs(l, k))

                elif left > right:
                    # Alice keeps the right side.
                    #
                    # As k increases, right only gets smaller,
                    # so if right * 2 <= ans, all later splits
                    # are useless.
                    if right * 2 <= ans:
                        break

                    ans = max(ans, right + dfs(k + 1, r))

                else:
                    # Equal sums: Alice can choose either side.
                    ans = max(
                        ans,
                        left + dfs(l, k),
                        right + dfs(k + 1, r)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)