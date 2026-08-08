                if right[j + 1] <= i:
                    break

                if word1[i] == word2[j]:
                    ans.append(i)
                    p = i
                    found = True
                    break

                if not used:
                    ans.append(i)
                    p = i
                    used = True
                    found = True
                    break

            if not found:
                return []

        return ans
