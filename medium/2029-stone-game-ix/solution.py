class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        # Stones divisible by 3 don't change the sum modulo 3.
        # They can effectively be used as extra moves.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # Odd number of 0-modulo stones
        return abs(cnt[1] - cnt[2]) > 2
