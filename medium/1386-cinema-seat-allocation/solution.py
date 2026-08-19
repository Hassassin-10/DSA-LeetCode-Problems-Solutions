class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Store reserved seats for only the rows that matter.
        rows = {}

        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << s)

        # Every completely free row can accommodate 2 groups.
        ans = (n - len(rows)) * 2

        for mask in rows.values():
            left = (mask & ((1 << 2) | (1 << 3) | (1 << 4) | (1 << 5))) == 0
            middle = (mask & ((1 << 4) | (1 << 5) | (1 << 6) | (1 << 7))) == 0
            right = (mask & ((1 << 6) | (1 << 7) | (1 << 8) | (1 << 9))) == 0

            if left and right:
                # Both non-overlapping blocks can be used.
                ans += 2
            elif left or middle or right:
                # At least one valid block exists.
                ans += 1

        return ans