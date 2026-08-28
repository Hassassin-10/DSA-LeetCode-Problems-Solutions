class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        cnt = Counter(s)

        # Check whether a palindrome can be formed.
        odd = [c for c in cnt if cnt[c] % 2]
        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Build the smallest possible left half.
        left = []
        for c in sorted(cnt):
            left.extend([c] * (cnt[c] // 2))

        # Given a left half, construct the full palindrome.
        def palindrome(left):
            return "".join(left) + middle + "".join(left[::-1])

        # We need the first palindrome strictly greater than target.
        #
        # Iterate through possible left halves in lexicographical order.
        # Instead of generating all permutations, find the smallest
        # permutation whose palindrome is > target.

        m = len(left)

        # Find the first left half >= target[:m].
        # If equal, the middle/right half determines whether it is > target.
        target_left = target[:m]

        # Standard "smallest multiset permutation >= target_left".
        def next_geq(target_left):
            a = left[:]

            # Try to construct target_left exactly.
            used = [0] * 26
            for c in a:
                used[ord(c) - 97] += 1

            prefix = []

            for i in range(m):
                t = ord(target_left[i]) - 97

                # Exact match is possible.
                if used[t] > 0:
                    prefix.append(chr(t + 97))
                    used[t] -= 1
                    continue

                # We cannot match target here.
                # Pick the smallest available character > target.
                for x in range(t + 1, 26):
                    if used[x] > 0:
                        prefix.append(chr(x + 97))
                        used[x] -= 1

                        for y in range(26):
                            prefix.extend([chr(y + 97)] * used[y])

                        return prefix

                # No larger character here: backtrack below.
                break

            else:
                # Exact target_left is possible.
                candidate = prefix
                p = palindrome(candidate)

                if p > target:
                    return candidate

            # Backtrack.
            for i in range(len(prefix) - 1, -1, -1):
                old = ord(prefix[i]) - 97
                used[old] += 1

                for x in range(old + 1, 26):
                    if used[x] > 0:
                        result = prefix[:i] + [chr(x + 97)]
                        used[x] -= 1

                        for y in range(26):
                            result.extend([chr(y + 97)] * used[y])

                        return result

            return None

        ans = next_geq(target_left)

        if ans is None:
            return ""

        result = palindrome(ans)

        return result if result > target else ""
