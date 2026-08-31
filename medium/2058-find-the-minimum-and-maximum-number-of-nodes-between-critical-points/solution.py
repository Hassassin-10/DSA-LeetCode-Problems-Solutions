            if is_max or is_min:
                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - last)

                last = pos

            prev = curr
            curr = next_node

        # Fewer than two critical points
        if first == last:
            return [-1, -1]

        # Distance between first and last critical points
        max_dist = last - first

        return [min_dist, max_dist]

