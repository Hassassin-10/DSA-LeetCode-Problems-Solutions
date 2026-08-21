from typing import List
from math import gcd


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove redundant coins:
        # if a coin is a multiple of another coin, its multiples
        # are already covered by the smaller coin.
        coins.sort()
        filtered = []

        for c in coins:
            if not any(c % x == 0 for x in filtered):
                filtered.append(c)

        coins = filtered
        n = len(coins)

        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b

        def count(x: int) -> int:
            """Number of distinct amounts <= x."""
            total = 0

            # Inclusion-exclusion over all subsets.
            for mask in range(1, 1 << n):
                cur_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        cur_lcm = lcm(cur_lcm, coins[i])

                        # No need to continue if LCM > x.
                        if cur_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                multiples = x // cur_lcm

                if bits & 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        # The answer is at most min(coins) * k.
        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo