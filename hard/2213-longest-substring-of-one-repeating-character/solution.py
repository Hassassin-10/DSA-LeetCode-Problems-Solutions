class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)

        # Each node:
        # [length, left_char, right_char, left_len, right_len, best]
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            length1, lc1, rc1, ll1, rl1, best1 = a
            length2, lc2, rc2, ll2, rl2, best2 = b

            length = length1 + length2
            left_char = lc1
            right_char = rc2

            # Length of prefix consisting of the same character
            left_len = ll1
            if ll1 == length1 and rc1 == lc2:
                left_len += ll2

            # Length of suffix consisting of the same character
            right_len = rl2
            if rl2 == length2 and rc1 == lc2:
                right_len += rl1

            # Best run completely inside either segment
            best = max(best1, best2)

            # Best run crossing the boundary
            if rc1 == lc2:
                best = max(best, rl1 + ll2)

            return (
                length,
                left_char,
                right_char,
                left_len,
                right_len,
                best
            )

        def build(node, l, r):
            if l == r:
                tree[node] = (1, s[l], s[l], 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, char):
            if l == r:
                tree[node] = (1, char, char, 1, 1, 1)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, char)
            else:
                update(node * 2 + 1, mid + 1, r, idx, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1][5])

        return ans