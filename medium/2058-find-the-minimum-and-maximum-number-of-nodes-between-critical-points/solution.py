class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            next_node = curr.next
            pos += 1

            # Check if curr is a local maximum or minimum
            is_max = curr.val > prev.val and curr.val > next_node.val
            is_min = curr.val < prev.val and curr.val < next_node.val

            if is_max or is_min:
                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = next_node

        # Fewer than two critical points
        if first == last:
            return [-1, -1]

        # Distance between first and last critical points
        max_dist = last - first

        return [min_dist, max_dist]
