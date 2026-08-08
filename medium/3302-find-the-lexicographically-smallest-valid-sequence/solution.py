                break
            if j == m:
        for i in range(n):

        j = 0
        mismatch = True
        ans = []
            i -= 1


            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif mismatch and (j == m - 1 or i < last[j + 1]):
                ans.append(i)
                j += 1
                mismatch = False

        return ans if j == m else []
