class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have more than k ones, so move left.
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # We have exactly k ones.
            if ones == k:
                # Remove leading zeros.
                while s[left] == '0':
                    left += 1

                curr = s[left:right + 1]

                # Choose shortest, then lexicographically smallest.
                if (not best or
                    len(curr) < len(best) or
                    (len(curr) == len(best) and curr < best)):
                    best = curr

        return best