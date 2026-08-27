        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        cnt = [0] * 26
        # Simpler O(26 * n) approach:

            pass
            # available characters for this suffix incrementally.
            # Instead of rebuilding cnt repeatedly, calculate the
            # Restore the characters used by target[0:i].
        for i in range(n - 1, -1, -1):
        # where we can make the first character strictly larger.
        # Try to construct a permutation that is > target.
        # We scan from right to left, looking for the position
        n = len(s)


        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        cnt = [0] * 26
    def lexGreaterPermutation(self, s: str, target: str) -> str:
class Solution:
