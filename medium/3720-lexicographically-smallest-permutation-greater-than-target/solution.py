class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Frequency of characters in s
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Try to make the answer greater at position i.
        # We go from right to left so that the first difference
        # happens as late as possible.
        for i in range(n - 1, -1, -1):
            # Recreate the available characters after using target[:i]
            rem = cnt[:]

            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if rem[x] == 0:
                    possible = False
                    break

                rem[x] -= 1

            if not possible:
                continue

            # Find the smallest character > target[i]
            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if rem[c] > 0:
                    rem[c] -= 1

                    # target[:i] + chosen larger character
                    ans = target[:i] + chr(ord('a') + c)

                    # Smallest possible suffix
                    for k in range(26):
                        ans += chr(ord('a') + k) * rem[k]

                    return ans

        return ""