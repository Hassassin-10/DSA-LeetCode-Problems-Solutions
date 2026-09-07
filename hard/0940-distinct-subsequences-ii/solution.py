class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp[i] = number of distinct non-empty subsequences
        # after processing s[:i]
        dp = 0

        # last[c] = number of distinct subsequences that existed
        # before the previous occurrence of character c
        last = [0] * 26

        for ch in s:
            c = ord(ch) - ord('a')

            # Every existing subsequence can append ch,
            # and ch itself forms a new subsequence.
            new_dp = (2 * dp + 1 - last[c]) % MOD

            # Save the old dp value for this character.
            last[c] = dp + 1
            dp = new_dp

        return dp
