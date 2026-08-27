                    # The prefix target[:i] has already consumed
                    # those characters, so construct the smallest suffix.

                    cnt[c] -= 1

                    prefix = target[:i] + chr(c)
                if cnt[c] > 0:
            for c in range(t + 1, 26):
                    suffix = []
                    for x in range(26):
                        suffix.append(chr(x + ord('a')) * cnt[x])

                    return prefix + ''.join(suffix)

            # Consume target[i] so we can continue matching it.
            if cnt[t] == 0:
                break
            cnt[t] -= 1

        return ""
