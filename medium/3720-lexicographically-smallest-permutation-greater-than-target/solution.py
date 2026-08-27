            if not possible:
                continue

            # At position i, choose the smallest character
            # strictly greater than target[i].
            t = ord(target[i]) - ord('a')

            for c in range(t + 1, 26):
                if remaining[c] > 0:
                    remaining[c] -= 1

                    ans = target[:i] + chr(c)

                    # Smallest possible suffix.
                    for x in range(26):
                        ans += chr(x + ord('a')) * remaining[x]

                    return ans

        return ""
        
