                break
            nxt[j] = p
            p -= 1

        ans, p, used = [], -1, False

        for j in range(m):
            for i in range(p + 1, nxt[j + 1]):
                if word1[i] == word2[j] or not used:
                    ans.append(i)
                    used |= word1[i] != word2[j]
                    p = i
                    break
            else:
                return []

        return ans
